import numpy as np
import matplotlib.pyplot as plt

def morph_polyhedra(start_points, end_points, steps):
    """Morphs one polyhedron into another over a number of steps."""
    morphs = []
    for t in np.linspace(0, 1, steps):
        interp = (1 - t) * np.array(start_points) + t * np.array(end_points)
        morphs.append(interp)
    return morphs

def points_to_midi(points):
    """Maps polyhedron points to MIDI notes (dummy function)."""
    # For demonstration: Normalize points and map to MIDI range
    points = np.array(points)
    midi_notes = np.clip((points.flatten() - points.min()) / (points.ptp() + 1e-9) * 127, 0, 127).astype(int)
    return midi_notes

def generate_music():
    # Example: Morph a cube into an octahedron
    cube = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]
    octahedron = [
        [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1], [0, 0, 0], [0, 0, 0]
    ]
    morphs = morph_polyhedra(cube, octahedron, steps=16)
    song = []
    for points in morphs:
        midi_notes = points_to_midi(points)
        song.append(midi_notes)
    print("Generated music sequence (MIDI notes):")
    print(song)
    # Optional: visualize morph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for points in morphs:
        ax.clear()
        ax.scatter(*zip(*points))
        plt.pause(0.1)
    plt.show()

if __name__ == "__main__":
    generate_music()