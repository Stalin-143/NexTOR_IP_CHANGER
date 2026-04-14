# NexTOR Debian Package Quick Reference

## Essential Commands

### Building

```bash
# Quick build (recommended)
debuild -us -uc

# Build with verbose output
debuild -v -us -uc

# Build binary only
debuild -us -uc -b

# Build source only
debuild -us -uc -S

# After build, check results
ls -lh ../nextor_*.deb
```

### Quality Assurance

```bash
# Check for Debian policy violations
lintian ../nextor_1.1-1_all.deb

# Show all issues including info
lintian -i ../nextor_1.1-1_all.deb

# Check specific category
lintian -t debian_policy ../nextor_1.1-1_all.deb
```

### Installation

```bash
# Standard installation
sudo dpkg -i ../nextor_1.1-1_all.deb

# Fix dependency issues
sudo apt-get install -f

# Reinstall (if corrupted)
sudo dpkg --configure nextor
sudo apt-get install --reinstall nextor

# Complete removal
sudo apt-get purge nextor
```

### Testing

```bash
# Verify installation
which nextor
dpkg -l | grep nextor

# Test command
nextor --help

# View documentation
man nextor

# Test Python imports
python3 -c "from Nex_Tor_IP_changer import NexTOR; print('OK')"
```

### Inspection

```bash
# Package contents
dpkg -c ../nextor_1.1-1_all.deb

# Installed files
dpkg -L nextor

# Package info
dpkg -I ../nextor_1.1-1_all.deb

# Installed details
dpkg -s nextor

# Extract for inspection
mkdir /tmp/nextor-check
dpkg-deb -x ../nextor_1.1-1_all.deb /tmp/nextor-check
find /tmp/nextor-check
```

### Cleanup

```bash
# Clean build artifacts
debclean

# Manual cleanup
rm -rf build/ dist/ *.egg-info/
rm -f debian/nextor/
rm -f ../nextor_*

# Full source clean
fakeroot debian/rules clean

# Remove extracted inspection
rm -rf /tmp/nextor-check
```

## Common Issues & Fixes

| Issue | Command/Solution |
|-------|------------------|
| Build tool missing | `sudo apt-get install devscripts debhelper` |
| Dependency error | `sudo apt-get build-dep .` |
| Permission denied | `chmod +x debian/rules` |
| Import error | `python3 -c "from Nex_Tor_IP_changer import NexTOR"` |
| nextor not found | `sudo dpkg -i ../nextor_*.deb && sudo apt-get install -f` |
| lintian errors | Review `DEBIAN_PACKAGING.md` for fixes |
| Git signing issues | `git config user.signingkey <KEY_ID>` |

## Directory Structure

```
NexTOR_IP_CHANGER/
├── debian/                     # Debian packaging files
│   ├── control                # Package metadata
│   ├── changelog              # Release history
│   ├── copyright              # License (MIT)
│   ├── rules                  # Build rules
│   ├── install                # File installation
│   ├── nextor.1               # Man page
│   ├── compat                 # Debhelper level 13
│   └── source/format          # Format v3
├── Nex_Tor_IP_changer/        # Main Python package
│   ├── __init__.py           # Package init
│   ├── NexTOR.py             # Main executable
│   ├── nex.py                # Helper functions
│   └── install.py            # Install utilities
├── setup.py                   # Python setup
├── pyproject.toml            # Modern Python build config
├── MANIFEST.in               # Build manifest
├── BUILD_INSTRUCTIONS.md     # Detailed build guide
├── DEBIAN_PACKAGING.md       # Debian standards guide
├── KALI_SUBMISSION.md        # Kali submission guide
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

## Build Process Flow

```
1. Install build tools
   └─> debhelper, dh-python, devscripts

2. Prepare source
   └─> Ensure debian/ directory present

3. Build package
   └─> debuild -us -uc

4. Run lintian
   └─> All errors must be fixed

5. Test installation
   └─> sudo dpkg -i, nextor command

6. Archive artifacts
   └─> Save nextor_1.1-1_all.deb

7. Submit to Kali (optional)
   └─> Follow KALI_SUBMISSION.md
```

## Package Metadata Quick View

```bash
# View package name and version
grep "^Package:\|^Version:" debian/control

# View dependencies
grep "^Depends:" debian/control

# View maintainer
grep "^Maintainer:\|^Uploaders:" debian/control

# View description
grep "^Description:" -A 10 debian/control
```

## For Kali Linux Submission

```bash
# 1. Update maintainer
nano debian/control  # Change Maintainer to Kali Linux

# 2. Update changelog
nano debian/changelog  # Add -1kali1 suffix

# 3. Push to GitLab
git add debian/
git commit -S -m "Prepare for Kali Linux"
git push origin submit/nextor-1.1

# 4. Create merge request on GitLab
# https://gitlab.com/kali-team/packages/nextor
```

## Performance Tips

```bash
# Parallel build (if available)
debuild -us -uc -j$(nproc)

# Faster cleanup
debclean -v

# Background build
debuild -us -uc &

# Check build progress
tail -f ../nextor_*.log
```

## Dependency Verification

```bash
# Check if dependencies are installed
apt-cache search python3-stem
apt-cache search python3-requests
apt-cache search tor

# Install dependencies for testing
sudo apt-get install python3-stem python3-requests tor

# Verify availability
python3 -c "import stem; print(stem.__version__)"
python3 -c "import requests; print(requests.__version__)"
```

## Version Scheme

**Current:** `1.1-1`

- `1.1` = Upstream version
- `-1` = Debian package revision

**For Future Updates:**

```
1.1-2    # Debian packaging fix (no code change)
1.2-1    # New upstream version
1.2-1kali1  # For Kali Linux submission
```

## Success Criteria

✓ All commands listed above complete without errors  
✓ `lintian` reports clean  
✓ Package installs and works  
✓ `nextor` command is available  
✓ Documentation is accessible via `man nextor`  
✓ Dependencies are properly resolved  

---

**Quick Links:**
- Detailed guide: [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)
- Debian standards: [DEBIAN_PACKAGING.md](DEBIAN_PACKAGING.md)
- Kali submission: [KALI_SUBMISSION.md](KALI_SUBMISSION.md)
- GitHub repo: https://github.com/Stalin-143/NexTOR_IP_CHANGER
