import character
import chapter_one

def exposite(text: tuple):
    for paragraph in text:
        # IF not the last paragraph, add a ... (press enter to continue)
        if paragraph != text[-1]:
            input(paragraph + "..[enter]")
        else:
            input(paragraph)

if __name__ == "__main__":
    exposite(chapter_one.backstory)
