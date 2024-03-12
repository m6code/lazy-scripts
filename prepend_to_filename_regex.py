import os
import re

# Get the current working directory
#path = os.getcwd()
#FileNames = os.listdir(path)
#for fileName in FileNames:
#    os.rename(fileName, fileName.replace("%20"," "))


def prepend_pattern_to_filename(filepath, pattern_regex):
  """
  Prepends the matched pattern found in the filename using the provided regex.

  Args:
    filepath: Path to the file.
    pattern_regex: The regex pattern to match within the filename.

  Returns:
    The new filename with the prepended pattern (if a match is found), 
    or None if no match or error occurs.
  """
  filename = os.path.basename(filepath)
  match = re.search(pattern_regex, filename)

  if match:
    # Extract the matched pattern
    matched_pattern = match.group().replace("[", "")
    # Construct the new filename with prepended pattern
    new_filename = f"{matched_pattern}. {filename}"
    # Rename the file
    try:
      os.rename(filepath, os.path.join(os.path.dirname(filepath), new_filename))
      return new_filename
    except OSError as e:
      print(f"Error renaming file {filepath}: {e}")
      return None
  else:
    print(f"No match found for pattern in {filepath}")
    return None

# Define the regex pattern
pattern_regex = r"\[[\d]{1,2} +"

# Get the directory path (replace 'path/to/your/directory' with your actual path)
directory_path = os.getcwd()

# Loop through files in the directory
for filename in os.listdir(directory_path):
  filepath = os.path.join(directory_path, filename)
  # Skip directories
  if os.path.isdir(filepath):
    continue

  # Prepend pattern and handle potential errors
  new_filename = prepend_pattern_to_filename(filepath, pattern_regex)

  # Print information about the renamed file (if successful)
  if new_filename:
    print(f"Renamed {filename} to {new_filename}")

