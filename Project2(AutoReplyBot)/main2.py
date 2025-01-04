import pyautogui
import pyperclip
import time

def main():
    # Pause between PyAutoGUI commands
    pyautogui.PAUSE = 0.5

    # Coordinates
    click_position = (1397, 1048)  # Position to click
    drag_start = (896,241)       # Starting position for drag
    drag_end = (920,935)       # Ending position for drag

    # Click at the specified position
    pyautogui.click(click_position)

    # Add a small delay to ensure any UI updates
    time.sleep(0.5)

    # Move to the drag starting position
    pyautogui.moveTo(drag_start)

    # Drag to the ending position while holding the mouse button
    pyautogui.mouseDown()
    pyautogui.dragTo(drag_end, duration=1, button='left')  # Drag with a smooth movement
    pyautogui.mouseUp()

    # Copy the selected text to the clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')

    # Pause to ensure clipboard data is updated
    time.sleep(0.5)

    # Retrieve text from clipboard
    selected_text = pyperclip.paste()

    # Output the text (for debugging or further processing)
    print("Selected Text:")
    print(selected_text)

    # Return the selected text
    return selected_text

if __name__ == "__main__":
    text = main()
