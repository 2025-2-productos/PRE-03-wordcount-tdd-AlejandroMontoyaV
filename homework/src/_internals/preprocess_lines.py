def preprocess_lines(all_lines):
    # preprocess lines by stripping whitespace and converting to lowercase
    all_lines = [line.strip().lower() for line in all_lines]
    return all_lines
