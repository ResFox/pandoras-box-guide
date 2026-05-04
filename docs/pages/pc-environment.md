# PC Environment

A correctly configured PC is the single biggest factor in stable performance. Go through this checklist **before** opening a support ticket.

## 1. Windows version

- **Windows 10 22H2** or **Windows 11 23H2 +** are recommended.
- Avoid Windows Insider / Dev / Canary builds — they break compatibility regularly.

## 2. BIOS / UEFI

Enable the following in BIOS:

- [x] **TPM 2.0**
- [x] **Secure Boot**
- [x] **Virtualization** (Intel: VT-x / VT-d • AMD: SVM / IOMMU)
- [x] **HVCI / Memory Integrity**

Then reboot, open `Core Isolation` in the Windows search bar, and confirm **Memory Integrity** is **ON**.

## 3. Display & scaling

- Resolution should match your monitor's native resolution.
- Game must run **borderless windowed** (not exclusive fullscreen).
- **Display scale** in Windows must be **100%**.
- **HDR off** while running the software.

## 4. Drivers

| Component | Recommendation |
|---|---|
| GPU | Latest **Game Ready** (NVIDIA) / **Adrenalin** (AMD) |
| Chipset | Latest from your motherboard vendor |
| Audio | Latest from vendor; avoid generic Microsoft drivers |
| Visual C++ | [All-in-one redistributable](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/) |
| DirectX | [DirectX End-User Runtime](https://download.microsoft.com/download/1/7/1/1718ccc4-6315-4d8e-9543-8e28a4e18c4c/dxwebsetup.exe) |

## 5. Antivirus

!!! warning
    The loader is heavily packed and *will* be flagged by Defender / third-party AV as a false positive. **Add an exclusion** for the cheat folder, or disable real-time protection while playing.

Best practice:

1. Settings → Privacy & security → Windows Security → Virus & threat protection.
2. **Manage settings → Exclusions → Add an exclusion → Folder**.
3. Select the folder where the loader lives.

## 6. Power & background

- Power plan: **Ultimate Performance** or **High Performance**.
- Disable **Game Bar** and **Game Mode** (Windows Settings → Gaming).
- Close OBS, Discord overlays, RGB tools, and browser before launching.

## 7. Verify with the checker

Run the checker tool from the Discord pinned messages — it confirms TPM / Secure Boot / HVCI / Vanguard state in one go.
