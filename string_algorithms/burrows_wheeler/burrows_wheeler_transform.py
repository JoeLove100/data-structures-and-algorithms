from collections import deque


def get_bw_transform(text: str) -> str:
    """
    return the Burrows-Wheeler transform of
    text
    """

    text = deque(text)
    rotations = []

    for _ in range(len(text)):
        text.rotate(1)
        rotations.append(list(text).copy())

    rotations = sorted(rotations)  # sorts lexicographically by default
    bw_transformed_text = "".join([s[-1] for s in rotations])
    return bw_transformed_text


if __name__ == "__main__":

    txt = input().strip()
    print(get_bw_transform(txt))
