# GitHub Upload Steps

## Recommended repository name

```text
kirsten-work-os-kernel
```

## Upload option A: GitHub web upload

1. Create a new GitHub repository.
2. Keep it public only if you are comfortable with the included profile and career evidence being visible.
3. Unzip `kirsten-work-os-kernel.zip`.
4. Open the unzipped folder.
5. Drag the **contents** of the folder into GitHub upload, not the folder itself.
6. Commit with message: `Initialize Kirsten Work OS Kernel`.
7. Open the Actions tab and confirm the `ci` workflow runs.

## Upload option B: local git command line

```bash
git clone https://github.com/<your-user>/kirsten-work-os-kernel.git
cd kirsten-work-os-kernel
# copy the unzipped files into this folder
git add .
git commit -m "Initialize Kirsten Work OS Kernel"
git push origin main
```

## Expected green checks

The workflow should run tests, validation, sample branch generation, sample brief generation, and sample signal intake.
