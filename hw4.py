web_development =["Abhi","Megha","Sneha"]
data_science = ["Aishu","Alna","Misa"]
UI_UX_design = ["Krishna","Ansi","Durga"]

all_participants = [web_development, data_science,UI_UX_design]
#print(all_participants)
web_development.append("Limbi")
# print(web_development)
data_science.insert(1,"Sree")
# print(data_science)
UI_UX_design.pop()
# print(UI_UX_design)
new_DS = data_science.copy()
print("New datascience list:",new_DS)
data_science.clear()
print("First two participants in the web development:",web_development[0:2])
length=[len(x) for x in new_DS]
print("length of datascience participants:",length)

is_Asha_present = any("Asha" in workshop for workshop in all_participants)
print("Is Asha in all participants:", is_Asha_present)

my_tuple = (all_participants[0][0], new_DS[0], all_participants[2][0])
print("tuple of first participants from each domain:",my_tuple)

# You are organizing participants for three different workshops in a coding bootcamp: Web Development, Data Science, and UI/UX Design.
# Create a list for each workshop containing the names of 3 participants.
# Combine all three workshop lists into a single nested list called all_participants.
# A new participant joins the Web Development workshop — add their name to that list.
# Insert one more participant at the 2nd position in the Data Science list.
# Remove the last participant from the UI/UX Design list.
# Copy the list of Data Science participants to a new list and clear the original.
# From the Web Development list, display only the first two participants.
# Use list comprehension to create a list of the length of each name in the copied Data Science list.
# Check whether “Asha” is in any of the workshop lists.
# Finally, create a tuple that stores the name of the first participant from each workshop list (use slicing and indexing as needed).


