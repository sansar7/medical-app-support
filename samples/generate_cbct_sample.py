#!/usr/bin/env python3
"""Generate a fictional geometric DICOM phantom, never a patient scan.

Usage: python3 Tools/generate_review_sample.py /tmp/CBCT-Synthetic-Review
The phantom demonstrates import, display, measurement and exports. Its shapes
are not anatomy or a segmentation reference. Only Python's standard library is
required. Output is intentionally excluded from the app source repository.
"""
import argparse
import math
from pathlib import Path
import struct


def element(group, tag, vr, value):
    if isinstance(value, str):
        value = value.encode("ascii")
    if len(value) % 2:
        value += b"\0" if vr in ("UI", "OB", "OW") else b" "
    header = struct.pack("<HH", group, tag) + vr.encode("ascii")
    if vr in ("OB", "OW", "SQ", "UN", "UT"):
        return header + b"\0\0" + struct.pack("<I", len(value)) + value
    return header + struct.pack("<H", len(value)) + value


def generate(folder):
    folder.mkdir(parents=True, exist_ok=False)
    side, depth, spacing = 96, 64, 0.5
    study = "2.25.191984172716667603145153417392544549371"
    series = "2.25.191984172716667603145153417392544549372"
    sop_class = "1.2.840.10008.5.1.4.1.1.2"
    for z in range(depth):
        sop = f"2.25.191984172716667603145153417392544550{z:03d}"
        meta = b"".join([
            element(2, 1, "OB", b"\0\1"), element(2, 2, "UI", sop_class),
            element(2, 3, "UI", sop), element(2, 16, "UI", "1.2.840.10008.1.2.1"),
            element(2, 18, "UI", "2.25.191984172716667603145153417392544549373"),
        ])
        data = bytearray(b"\0" * 128 + b"DICM" + element(2, 0, "UL", struct.pack("<I", len(meta))) + meta)
        fields = [
            (8, 8, "CS", "DERIVED\\SECONDARY"), (8, 22, "UI", sop_class), (8, 24, "UI", sop),
            (8, 96, "CS", "CT"), (8, 4158, "LO", "SYNTHETIC GEOMETRIC PHANTOM - NOT A PATIENT"),
            (16, 16, "PN", "SYNTHETIC^PHANTOM"), (16, 32, "LO", "SYNTHETIC-NO-PATIENT"),
            (24, 80, "DS", str(spacing)),
            (32, 13, "UI", study), (32, 14, "UI", series), (32, 19, "IS", str(z + 1)),
            (32, 50, "DS", f"0\\0\\{z * spacing}"), (32, 55, "DS", "1\\0\\0\\0\\1\\0"),
            (40, 2, "US", struct.pack("<H", 1)), (40, 4, "CS", "MONOCHROME2"),
            (40, 16, "US", struct.pack("<H", side)), (40, 17, "US", struct.pack("<H", side)),
            (40, 48, "DS", f"{spacing}\\{spacing}"),
            (40, 256, "US", struct.pack("<H", 16)), (40, 257, "US", struct.pack("<H", 12)),
            (40, 258, "US", struct.pack("<H", 11)), (40, 259, "US", struct.pack("<H", 0)),
            (40, 4176, "DS", "1000"), (40, 4177, "DS", "2000"),
            (40, 4178, "DS", "0"), (40, 4179, "DS", "1"),
        ]
        for field in fields:
            data.extend(element(*field))
        pixels = bytearray()
        for y in range(side):
            for x in range(side):
                radius = math.hypot((x - 47.5) / 32, (y - 45) / 29)
                shell = 0.82 < radius < 1 and y < 70 and (12 < z < 27 or 38 < z < 50)
                value = 2200 if shell else (350 if radius < 1.15 and 7 < z < 57 else 0)
                # Independent spheres and a cube make orientation recognizable.
                if (x - 30)**2 + (y - 36)**2 + (z - 32)**2 < 49:
                    value = 3400
                if 59 <= x < 68 and 28 <= y < 39 and 28 <= z < 37:
                    value = 2800
                pixels.extend(struct.pack("<H", value))
        data.extend(element(0x7FE0, 0x0010, "OW", pixels))
        (folder / f"phantom-{z + 1:03d}.dcm").write_bytes(data)
    (folder / "README.txt").write_text(
        "Entirely computer-generated geometric phantom. No patient data.\n"
        "96 x 96 x 64 voxels, 0.5 mm spacing. Not anatomy or clinical validation.\n"
        "Open this folder with Dental CBCT Studio.\n", encoding="utf-8")
    print(f"Generated {depth} synthetic DICOM slices in {folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    generate(parser.parse_args().folder)
