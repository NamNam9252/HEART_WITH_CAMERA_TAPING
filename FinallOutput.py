import subprocess
import sys
import threading
import cv2
import os
import time
import turtle
import math

def install_package(package_name="opencv-python"):
    """Install a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f'Successfully installed {package_name}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to install {package_name}. Error: {e}')

def capture_images(num_images=5):
    """Capture images from the webcam and save them."""
    save_directory = os.getcwd()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Capturing images...")

    for i in range(num_images):
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        filename = os.path.join(save_directory, f'image_{i + 1}.png')
        cv2.imwrite(filename, frame)
        print(f'Image {i + 1} saved as {filename}')
        
        time.sleep(1)  # Wait 1 second between captures

    cap.release()
    cv2.destroyAllWindows()
    print("Finished capturing images.")

def draw_heart():
    """Draw a heart using Turtle graphics."""
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.pensize(2)
    turtle.color("red")

    num_lines = 200

    for i in range(num_lines):
        angle = (i / num_lines) * (2 * math.pi)
        x = 16 * (math.sin(angle) ** 3)
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        
        scale = 10
        turtle.goto(x * scale, y * scale)
        turtle.pendown()
        turtle.goto(0, 0)
        turtle.penup()

    turtle.goto(0, -220)
    turtle.pendown()
    turtle.color("black")
    turtle.write("SEND THE PIC THAT WAS SAVED IN SAME FOLDER", align="center", font=("Arial", 16, "normal"))
    turtle.penup()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    package_name = 'opencv-python'
    install_package(package_name)

    # Start capturing images in a separate thread
    capture_thread = threading.Thread(target=capture_images)
    capture_thread.start()

    # Draw heart in the main thread
    draw_heart()

    # Wait for the capture thread to finish
    capture_thread.join()
