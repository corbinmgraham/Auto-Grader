import sys

def get_ftext(text):
    return None # Returns formatted text

def process_image(scan):
    return None # Returns text

def scan_image(file):
    return None # Returns image

def process_source(image=None, text=None):
    # Process image or text
    return None

def get_outcome(input: None, source: None) -> None:
    return None

# get_outcome(input: Model, source: Model): -> statistic: Container

def print_stat(outcome):
    # Format and Print outcome
    print(f"Accuracy of Assignment: {outcome}")
    return None

def main():
    text_if = get_ftext(
        process_image(scan_image(None))) # --> File
    text_sf = get_ftext(process_source())
    print_stat(get_outcome(text_if, text_sf))
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)