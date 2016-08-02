
# TO DO: IMPLEMENT STEPS BELOW
# --
# 1. Properly structure output data from Classifier to fit Civic Graph table schema
# 2. Makes a POST to Civic Graph database with structured output data
# 3. Add new table to Civic Graph schema for data pulled from Classifier
# 4. Document POST functionality in API documentation

# ---
# Data associated with test dataset:
#
#  - List of Tokens (strings)
#     - List of label_accuracy_scores for each token (floats)
#     - boolean_label_list for each token (booleans or integers)
#     - List of named entities that exist in each token
#     - List of entity_relations (connections) that exist within each token

# ---
# Steps 1-2: Algorithm for structuring output data
#
# Generate label list for each token (can put this in algorithm.py)
# for each token in test_data_tokens:
#   create list of all label_accuracy_scores computed by classifier
#   e.g. token_1 = [0.13, ..., 0.88]
#        where len(token_1) = 5 and
#        token_1[0] = funding_accuracy and 
#        token_1[5] = location_accuracy

#   for each label_accuracy_score in the list:
#     check if at least one score is >= THRESHOLD
#     create boolean_label_list of length 6
#     if True:
#       means that at least one label applies to the token
#       e.g. token1 = [0, ..., 1, 0]
#            where token1[i] = 1
#              if label_accuracy_score >= THRESHOLD for that label
#              else token1[i] = 0
#     else:
#       means that all accuracy scores were < THRESHOLD so no labels apply to that token
#       therefore, set first five values boolean_label_list to 0 and
#       set 6th value in boolean_label_list (corresponds to "OTHER/UNDEFINED") = 1
#       append each boolean_label_list to all_label_lists

# ---
# Steps 3-4: Algorithm to POST structured output data to Civic Graph
#
# for each token in test_data_tokens:
#   extract entities within token
#   e.g. "Barack Obama works for the U.S. Government"
#         entities = [Barack Obama, U.S. Government
#   for each boolean_label_list in all_label_lists:
#     extract relations associated with a given label
#     e.g. Option 1: Separate list for each label
#                    employment_relations = [works for]
#          Option 2: Single list for all relations within token
#                    all_relations = [works for]
#   # posting entities
#   for each entity in entities:
#     check if entity exists within Civic Graph database
#     if True:
#       skip
#     else:
#       POST entity in Civic Graph entities table WHERE entity_type = Government
#       generate uniqueID for the entity
#   # post relations
#   for each relation in all_relations: (following Option 2 above)
#       query connections associated with each entity in token to check if that collaboration type already exists
#       if True:
#         skip
#       else:
#         POST collaboration under entity WHERE collaboration_type = employment
#         Note: If connection_type is bidirectional, POST for both entities



