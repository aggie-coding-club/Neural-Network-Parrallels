from flask import Flask, request, jsonify
from google_scrape import get_docs_data
from embedd import bert_vector_maker
from add_data import addmy_data
from access_database import search_database
from summarize.py import get_summary




@app.route('/process', methods=['POST'])
def full_process():
    data = request.json
    # this is the users prompt
    query = data.get("query", "")
    
    if query == "":
        return jsonify({"error": "Please provide a query"}), 400

    # Scrape websites, get text data, and embed it
    docs_data = get_docs_data(query)
    embeddings = [bert_vector_maker(doc['text']) for doc in docs_data]

    # Add the data to the database
    collection_name = 'maincollection'
    addmy_data(collection_name, docs_data, embeddings)

    """chroma db does have their own embeddings we can use as well and we dont need to add our own 
    you can run it as so:
    addmy_data(collection_name, docs_data) if we do do that tho search_results will call an error
    because in it we used different embeddings for the prompt/query or whatever so then we would have to 
    do this:
    thecollection = main_client.get_collection(collection_name)
    results = main_client.thecollection.query(query_text=query, n_results=3)
    so search_results = results"""

    # Search the database for similar documents
    search_results = search_database(query)

    

    # Get summaries for the top results
    summaries = [get_summary(text) for text in search_results['documents'][0]]
    """if this ever returns an error try this:
    summaries = [get_summary(text) for text in search_results.get("documents", [[]])[0]]
    if that doesn't work then oh boy idk"""

    return jsonify({"query": query, "results": search_results, "summaries": summaries})

if __name__ == '__main__':
    app.run(debug=True)