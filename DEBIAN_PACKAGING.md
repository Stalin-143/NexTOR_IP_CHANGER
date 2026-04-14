# Debian Packaging Guide for NexTOR IP Changer

This guide provides complete instructions for building, testing, and deploying the NexTOR IP Changer as a Debian package.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Package Structure](#package-structure)
4. [Building the Package](#building-the-package)
5. [Testing the Package](#testing-the-package)
6. [Installation](#installation)
7. [Troubleshooting](#troubleshooting)

## Overview

**Package Name:** nextor  
**Version:** 1.1  
**License:** MIT  
**Architecture:** all (architecture-independent)  
**Section:** utils  

NexTOR IP Changer is a command-line tool for rotating Tor exit nodes and changing your public IP address dynamically.

## Prerequisites

### Required Tools

```bash
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    debhelper \
    dh-python \
    python3-setuptools \
    python3-all \
    devscripts \
    lintian \
    fakeroot \
    git
```

### System Requirements

- Debian-based system (Ubuntu, Kali Linux, etc.)
- Python 3.6 or later
- Git (for version control)

## Package Structure

The complete Debian package structure is as follows:

```
NexTOR_IP_CHANGER/
├── debian/                      # Debian packaging files
│   ├── control                 # Package metadata
│   ├── changelog               # Release history
│   ├── copyright               # License information
│   ├── rules                   # Build rules
│   ├── install                 # File installation instructions
│   ├── nextor.1                # Man page
│   ├── compat                  # Debhelper compatibility level
│   └── source/
│       └── format              # Source format specification
├── Nex_Tor_IP_changer/        # Python package directory
│   ├── __init__.py            # Package initialization
│   ├── NexTOR.py              # Main executable
│   ├── nex.py                 # Utility functions
│   └── install.py             # Installation utilities
├── setup.py                    # Python package setup
├── pyproject.toml             # Build system configuration
├── MANIFEST.in                # Build manifest
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

### Debian Files Explained

#### `debian/control`
- **Source:** Package source metadata
- **Package:** Binary package configuration
- Dependencies (Depends, Recommends, Conflicts)
- Homepage, version control links

#### `debian/changelog`
- Maintains release history
- Required Debian policy file
- Format: `package (version) distribution; urgency=level`

#### `debian/copyright`
- Specifies licensing information
- Lists copyright holders
- Required by Debian policy

#### `debian/rules`
- Makefile for building the package
- Uses debhelper (dh)
- Automates compilation and installation

#### `debian/install`
- Specifies which files to install
- Format: `source destination`
- Example: `NexTOR.py usr/share/nextor/`

#### `debian/nextor.1`
- Man page (documentation)
- Accessed via `man nextor`
- Standard Debian documentation file

#### `debian/source/format`
- Specifies packaging format: `3.0 (quilt)` for source format v3

#### `debian/compat`
- Debhelper compatibility level
- Current standard: level 13

## Building the Package

### Step 1: Prepare the Build Environment

```bash
cd /path/to/NexTOR_IP_CHANGER
```

### Step 2: Install Build Dependencies

```bash
sudo apt-get build-dep .
```

Or manually:

```bash
sudo apt-get install -y \
    debhelper-compat \
    dh-python \
    python3-setuptools \
    python3-all
```

### Step 3: Build the Package

#### Option A: Using `debuild` (Recommended)

```bash
debuild -us -uc
```

**Flags Explanation:**
- `-us`: Don't sign source file
- `-uc`: Don't sign changes file

**Output Files:** Generated in parent directory
- `nextor_1.1-1_all.deb` - Binary package
- `nextor_1.1-1.dsc` - Source package description
- `nextor_1.1-1.tar.gz` - Source tarball
- `nextor_1.1-1_amd64.changes` - Changes file

#### Option B: Using `dpkg-buildpackage`

```bash
dpkg-buildpackage -us -uc -b
```

**Flags:**
- `-us`: Don't sign source file
- `-uc`: Don't sign changes file
- `-b`: Build binary package only

#### Option C: Using `debuild` with Signing (Release)

```bash
debuild -S
```

This creates signed source package for upload to repositories.

### Step 4: Check Build Output

```bash
ls -lh ../nextor*.deb
file ../nextor_1.1-1_all.deb
```

## Testing the Package

### 1. Linting with `lintian`

Check for Debian Policy violations:

```bash
lintian -i ../nextor_1.1-1_all.deb
```

**Output Levels:**
- `E:` - Error (must fix)
- `W:` - Warning (should fix)
- `I:` - Info (informational)
- `N:` - Note (minor issue)

### 2. Installation Test

```bash
# Install the package
sudo dpkg -i ../nextor_1.1-1_all.deb

# Verify installation
dpkg -l | grep nextor
which nextor

# Check installed files
dpkg -L nextor
```

### 3. Functional Testing

```bash
# Check dependencies
nextor --help 2>&1 || echo "May require manual setup"

# View man page
man nextor

# Test import
python3 -c "from Nex_Tor_IP_changer import NexTOR; print('Import successful')"
```

### 4. Uninstall Test

```bash
sudo apt-get remove nextor
sudo apt-get purge nextor
```

Verify clean removal:

```bash
dpkg -L nextor 2>&1 | grep "No such file"
```

## Installation

### Method 1: Installation from Built Package

```bash
sudo dpkg -i nextor_1.1-1_all.deb
sudo apt-get install -f  # Fix any dependency issues
```

### Method 2: Installation from Repository (Future)

When the package is added to Kali Linux repository:

```bash
sudo apt-get update
sudo apt-get install nextor
```

### Post-Installation

1. Ensure Tor is installed and running:

```bash
sudo apt-get install tor
sudo systemctl enable tor
sudo systemctl start tor
```

2. Verify installation:

```bash
nextor --help
man nextor
```

## Build Troubleshooting

### Common Issues

#### 1. "Package not found" or dependency errors

**Solution:**
```bash
sudo apt-get update
sudo apt-get install -y python3-setuptools dh-python
```

#### 2. "Permission denied" during build

**Solution:**
```bash
chmod +x debian/rules
sudo chown $USER:$USER -R .
```

#### 3. `lintian` reports errors

**Common errors and fixes:**

| Error | Solution |
|-------|----------|
| `E: changelog-is-dh_make-template` | Update changelog with real changes |
| `W: maintainer-not-in-uploaders` | Add maintainer to Uploaders field |
| `W: missing-upstream-changelog` | Add upstream changelog |
| `E: missing-build-depends` | Add missing tool to Build-Depends |

#### 4. Build fails with "missing dependency"

```bash
# Auto-install build dependencies
sudo apt-get build-dep .

# Or manually from debian/control
sudo apt-get install $(grep Build-Depends debian/control \
    | sed 's/.*: //; s/,.*//; s/\[.*\]//g')
```

#### 5. Python import errors

Ensure package has `__init__.py`:

```bash
touch Nex_Tor_IP_changer/__init__.py
```

### Debug Commands

```bash
# See full build process
debuild -v

# Extract and inspect binary package
dpkg-deb -x ../nextor_1.1-1_all.deb /tmp/nextor-inspect

# List package contents
dpkg -c ../nextor_1.1-1_all.deb

# Show package information
dpkg-deb -I ../nextor_1.1-1_all.deb

# Check dependencies
dpkg -I ../nextor_1.1-1_all.deb | grep Depends
```

## Clean Up

Clean build artifacts:

```bash
# Remove build directory
debclean

# Remove all build files
rm -f ../nextor*
rm -rf debian/nextor/
rm -rf build/ dist/ *.egg-info/

# Clean source tree
fakeroot debian/rules clean
```

## Checklist Before Release

- [ ] Version bumped in `debian/changelog`
- [ ] `lintian` reports no errors
- [ ] Package installs without errors
- [ ] `nextor` command works
- [ ] Man page is readable: `man nextor`
- [ ] All dependencies correct in `debian/control`
- [ ] Copyright file complete and accurate
- [ ] LICENSE file present
- [ ] README documentation up-to-date

## Additional Resources

- [Debian New Maintainers' Guide](https://www.debian.org/doc/manuals/debian-faq/)
- [Debian Policy Manual](https://www.debian.org/doc/debian-policy/)
- [Debhelper Documentation](https://manpages.debian.org/debhelper)
- [dh_python Documentation](https://manpages.debian.org/dh_python3)
- [Lintian Checks](https://lintian.debian.org/manual/section-2.3.html)
