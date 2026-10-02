import os
from pathlib import Path 
from dotenv import load_dotenv
from supabase import create_client, Client


os.chdir(Path(__file__).parent)


load_dotenv()


TABLE = "notes5"


# Create Instance from SupaBase Class
supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY"),
)

print (os.environ.get("SUPABASE_URL"))

def create_note(title, content):
    payload = {"title": title, "content": content}
    return supabase.table(TABLE).insert(payload).execute().data[0]

def list_notes():
    return supabase.table(TABLE).select("*").order("id").execute().data

def get_note(note_id):
    return supabase.table(TABLE).select("*").eq("id", note_id).execute().data

def update_note(note_id, **fields):

    updates = {k:v for k,v in fields.items() if v is not None}
    if not updates:
        raise ValueError("No fields to update")
    
    data = supabase.table(TABLE).update(updates).eq("id", note_id).execute().data 
    return data[0] if data else None 


def delete_note(note_id):
    data = supabase.table(TABLE).delete().eq("id", note_id).execute().data
    return bool(data)


def main():
    # 1 create note
    new_note = create_note("Einkaufsliste 9", "Milk, eggs, bread")
    print("created", new_note)

    # 2. Get all notes
    notes_list = list_notes()
    print("All Notes:", notes_list)


    # 3. Get speficif Note
    note = get_note(new_note["id"])
    print(note)

    # 4. Update Note
    updated_note = update_note(new_note["id"], title="Einkaufsliste 88", content="MIllllllk, eggggs")
    print(updated_note)

    # 5. Delete Note
    deleted = delete_note(new_note["id"])
    print(deleted)



if __name__ == "__main__":
    main()