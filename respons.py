import chromadb
from chromadb import PersistentClient

# ----------------------------------------
# Initialize Chroma Client (same path)
# ----------------------------------------
client = PersistentClient(path="./chroma_data")

collection = client.get_collection(name="tickets")

# ----------------------------------------
# Function to search tickets
# ----------------------------------------
def search_tickets(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results

# ----------------------------------------
# Function to format response
# ----------------------------------------
def format_response(results):
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "❌ No relevant tickets found."

    response = "🔍 Top Matching Tickets:\n\n"

    for i, (doc, meta) in enumerate(zip(documents, metadatas), start=1):
        response += f"--- Result {i} ---\n"
        response += f"🆔 Ticket ID: {meta.get('ticket_id')}\n"
        response += f"📌 Title: {meta.get('title')}\n"
        response += f"📊 Status: {meta.get('status')}\n"
        response += f"⚡ Priority: {meta.get('priority')}\n"
        response += f"🏷 Category: {meta.get('category')}\n"
        response += f"👤 Assigned To: {meta.get('assigned_to')}\n"
        response += f"📝 Content: {doc}\n\n"

    return response

# ----------------------------------------
# Main Execution
# ----------------------------------------
if __name__ == "__main__":
    user_query = input("Enter your query: ")

    results = search_tickets(user_query)
    final_output = format_response(results)

    print(final_output)