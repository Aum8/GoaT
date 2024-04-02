from nlp import spacy_processing

species = {'human': 'homo sapien'}
families = {"plant": "33090[Viridiplantae]",
             "butterfly": "7088[Lepidoptera]"}
kingdoms = {}
attributes = {'genome_size': 'genome_size'}  # Map human-readable attribute names to database field names

def process_question(question):
    tokens = spacy_processing(question)[1]

    query_parts = []
    for part in tokens:
        if part in families:
            query_parts.append(f'tax_name({families[part]})')
        elif any(alias in part.lower() for alias in attributes):  # Check for lowercase variations of attribute names
            comparison_index = tokens.index(part)
            next_word = tokens[comparison_index + 1]  # Assuming comparison operator follows attribute
            if next_word in ['<', '<=', '>', '>=', '=']:
                comparison_value = tokens[comparison_index + 2]  # Assuming value follows comparison operator
                query_parts.append(f"{attributes[attributes.get(part.lower())]} {next_word} {comparison_value}")
            else:
                # If no comparison, just include the attribute
                query_parts.append(f"{attributes.get(part.lower())}")

    query = ' AND '.join(query_parts)
    return query


question = "List the plants with genome_size > 1000."
print(process_question(question))
question = "List the butterfly species with genome_size = 1000."
print(process_question(question))
