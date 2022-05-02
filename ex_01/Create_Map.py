import tkinter as tk

root = tk.Tk()
# Create N frames on top of each other
N = 4
frames = []
for n in range(N):

    frame = tk.Frame(root)
    frame.pack(side='top', anchor='w')
    # Store the current frame reference in"frames"
    frames.append(frame)

# Add some widgets in each frame
entryboxes = {frame: [] for frame in frames}

# Set entries to input screen size and map size
label_1 = tk.Label(frames[0], text="SCREEN_WIDTH")
label_1.pack(side='left')
e_1 = tk.Entry(frames[0], width=30)
e_1.pack(side='right')
entryboxes[frames[0]].append(e_1)
label_2 = tk.Label(frames[1], text="SCREEN_HEIGHT")
label_2.pack(side='left')
e_2 = tk.Entry(frames[1], width=29)
e_2.pack(side='right')
entryboxes[frames[1]].append(e_2)
label_3 = tk.Label(frames[2], text="MAP_WIDTH")
label_3.pack(side='left')
e_3 = tk.Entry(frames[2], width=33)
e_3.pack(side='right')
entryboxes[frames[2]].append(e_3)
label_4 = tk.Label(frames[3], text="MAP_HEIGHT")
label_4.pack(side='left')
e_4 = tk.Entry(frames[3], width=32)
e_4.pack(side='right')
entryboxes[frames[3]].append(e_4)

# Launch the app
root.mainloop()
