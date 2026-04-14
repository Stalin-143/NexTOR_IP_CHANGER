# Complete Build Instructions for NexTOR IP Changer Debian Package

## Quick Start

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y build-essential debhelper dh-python python3-setuptools devscripts

# Build the package
debuild -us -uc

# Test the package
lintian -i ../nextor_1.1-1_all.deb

# Install it
sudo dpkg -i ../nextor_1.1-1_all.deb
sudo apt-get install -f
```

## Detailed Build Process

### Phase 1: Environment Setup

#### 1.1 Install Build Tools

```bash
# Update package lists
sudo apt-get update

# Install essential build tools
sudo apt-get install -y \
    build-essential \
    debhelper \
    dh-python \
    devscripts \
    python3-setuptools \
    python3-all \
    lintian \
    fakeroot

# Optional: for signing and advanced operations
sudo apt-get install -y \
    git-buildpackage \
    pristine-tar \
    gnupg \
    gpg-agent
```

#### 1.2 Configure Git (for commit signing)

```bash
# Set up Git identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# If you want to sign releases (recommended)
# First, generate a GPG key if you don't have one
gpg --gen-key

# List your keys
gpg --list-keys

# Configure Git to use your signing key
git config --global user.signingkey <YOUR_KEY_ID>
git config --global commit.gpgsign true
```

#### 1.3 Verify Installation

```bash
# Check debhelper version
dh --version

# Check python tools
python3 --version
python3 -m pip --version

# Check dpkg-buildpackage
dpkg-buildpackage --version
```

### Phase 2: Source Preparation

#### 2.1 Navigate to Project Directory

```bash
cd /path/to/NexTOR_IP_CHANGER
```

#### 2.2 Verify Project Structure

```bash
# Expected structure:
find . -maxdepth 2 -type f | grep -E "(debian/|setup.py|pyproject.toml)" | sort
```

Should output:
```
./debian/control
./debian/changelog
./debian/copyright
./debian/rules
./debian/install
./debian/nextor.1
./debian/compat
./debian/source/format
./setup.py
./pyproject.toml
```

#### 2.3 Clean Previous Builds

```bash
# Remove old build artifacts
debclean

# Or manually remove
rm -rf build/ dist/ *.egg-info/
rm -f debian/nextor/
rm -f ../nextor_*
```

### Phase 3: Building the Package

#### 3.1 Build with debuild (Recommended Method)

```bash
# Navigate to project root
cd /path/to/NexTOR_IP_CHANGER

# Build binary package only (unsigned)
debuild -us -uc -b

# Or build source and binary (for full release)
debuild -us -uc

# With detailed output
debuild -v -us -uc
```

**Build Output:** (in parent directory)
```
../nextor_1.1-1_all.deb         # Binary package
../nextor_1.1-1_amd64.changes   # Changes file
../nextor_1.1-1.dsc             # Source description (if building -S)
../nextor_1.1-1.tar.gz          # Source tarball (if building -S)
../nextor_1.1-1.tar.xz          # Source tarball XZ (if building -S)
```

#### 3.2 Alternative: Build with dpkg-buildpackage

```bash
# Install build dependencies first
sudo apt-get build-dep .

# Build binary package
dpkg-buildpackage -us -uc -b

# Build everything (with signing)
dpkg-buildpackage -k<KEY_ID>
```

#### 3.3 Verify Build Success

```bash
# Check package was created
ls -lh ../nextor_*.deb

# Examine package details
file ../nextor_1.1-1_all.deb

# Show package info
dpkg-deb -I ../nextor_1.1-1_all.deb
```

### Phase 4: Quality Assurance Testing

#### 4.1 Lintian Analysis

```bash
# Basic lintian check
lintian ../nextor_1.1-1_all.deb

# Detailed (with explanations)
lintian -i ../nextor_1.1-1_all.deb

# Show all severity levels
lintian --display-info ../nextor_1.1-1_all.deb

# Check for specific category
lintian -t debian_policy ../nextor_1.1-1_all.deb
```

**Expected Output:** Clean or only informational messages

#### 4.2 Manual Package Inspection

```bash
# Extract package to temporary location
mkdir /tmp/nextor-inspect
dpkg-deb -x ../nextor_1.1-1_all.deb /tmp/nextor-inspect

# Browse extracted files
tree /tmp/nextor-inspect
cd /tmp/nextor-inspect && find . -type f | sort

# Check key files exist
ls -la /tmp/nextor-inspect/usr/bin/nextor
ls -la /tmp/nextor-inspect/usr/share/man/man1/nextor.1*
```

#### 4.3 Dependency Verification

```bash
# Extract and analyze dependencies
dpkg-deb -f ../nextor_1.1-1_all.deb Depends

# Verify each dependency is installable
apt-cache search python3-stem
apt-cache search python3-requests
apt-cache search tor

# Check package provides
dpkg-deb -f ../nextor_1.1-1_all.deb Provides
```

### Phase 5: Installation and Functional Testing

#### 5.1 Test Installation

```bash
# Install the package
sudo dpkg -i ../nextor_1.1-1_all.deb

# If dependency issues, use apt to fix
sudo apt-get install -f

# Verify installation
dpkg -l | grep nextor
which nextor
```

#### 5.2 Functional Testing

```bash
# Test command availability
nextor --help 2>&1 || echo "Command executed"

# View man page
man nextor

# Check file permissions
ls -la /usr/bin/nextor
ls -la /usr/share/doc/nextor/

# Test Python imports
python3 -c "from Nex_Tor_IP_changer import NexTOR; print('✓ Import successful')"

# Verify dependencies are accessible
python3 -c "import requests; print('✓ requests available')"
python3 -c "import stem; print('✓ stem available')"
```

#### 5.3 Uninstallation Testing

```bash
# Remove package
sudo apt-get remove nextor

# Verify clean removal of package files
dpkg -L nextor 2>&1 | head -5

# Completely remove (purge config files)
sudo apt-get purge nextor

# Verify complete removal
which nextor || echo "✓ nextor fully removed"
```

### Phase 6: Build Artifact Management

#### 6.1 Archive Build Products

```bash
# Create build artifacts directory
mkdir -p ~/nextor-builds/v1.1-1

# Copy build artifacts
cp ../nextor_1.1-1_all.deb ~/nextor-builds/v1.1-1/
cp ../nextor_1.1-1_amd64.changes ~/nextor-builds/v1.1-1/
cp ../nextor_1.1-1.dsc ~/nextor-builds/v1.1-1/  # if available
cp ../nextor_1.1-1.tar.* ~/nextor-builds/v1.1-1/  # source archives

# List archived artifacts
ls -lh ~/nextor-builds/v1.1-1/
```

#### 6.2 Create Build Summary

```bash
# Generate build info
cat > ~/nextor-builds/v1.1-1/BUILD_INFO.txt << 'EOF'
NexTOR IP Changer Debian Package Build
======================================

Build Date: $(date)
Package Version: 1.1-1
Architecture: all
Distribution: Debian/Kali Linux

Build System Information
------------------------
Debian/Ubuntu Version: $(lsb_release -ds)
Kernel: $(uname -r)
Python: $(python3 --version)
Build Tools: debhelper $(dh --version), dpkg-buildpackage

Build Command Used
------------------
debuild -us -uc

Quality Assurance
-----------------
Lintian Status: PASSED
Installation Test: PASSED
Functional Test: PASSED

Artifacts Included
------------------
- nextor_1.1-1_all.deb (Binary package)
- nextor_1.1-1_amd64.changes (Changes file)
- nextor_1.1-1.dsc (Source description) [if available]
- nextor_1.1-1.tar.* (Source archives) [if available]

Installation Instructions
--------------------------
sudo dpkg -i nextor_1.1-1_all.deb
sudo apt-get install -f
EOF

cat ~/nextor-builds/v1.1-1/BUILD_INFO.txt
```

## Troubleshooting

### Build Failures

#### Error: "Build-depends not satisfied"

```bash
# Install missing build dependencies
sudo apt-get build-dep .

# Or manually install from control file
sudo apt-get install debhelper-compat dh-python python3-setuptools
```

#### Error: "debuild command not found"

```bash
# Install devscripts package
sudo apt-get install devscripts

# Verify installation
devscripts --version
```

#### Error: "Permission denied" on debian/rules

```bash
# Make rules executable
chmod +x debian/rules

# Or during first build
debuild -us -uc
```

#### Error: "Package has no source"

```bash
# Ensure you're in the correct directory
pwd
ls -la debian/control

# Ensure debian/ directory exists
[ -d debian ] && echo "debian/ exists" || echo "Missing debian/"
```

### Package Installation Failures

#### Error: "dependency issues / unmet dependencies"

```bash
# Preview dependencies before installing
dpkg -I ../nextor_1.1-1_all.deb | grep Depends

# Install with dependency resolution
sudo apt-get install -y tor python3-stem python3-requests
sudo dpkg -i ../nextor_1.1-1_all.deb
sudo apt-get install -f
```

#### Error: "Package conflicts with installed version"

```bash
# Remove conflicting package first
sudo apt-get remove nextor-ip-changer

# Or purge to remove config files
sudo apt-get purge nextor-ip-changer

# Then install new package
sudo dpkg -i ../nextor_1.1-1_all.deb
```

### Runtime Failures

#### Error: "nextor: command not found"

```bash
# Verify installation
dpkg -l | grep nextor

# Check binary exists and is executable
ls -la /usr/bin/nextor

# Verify PATH includes /usr/bin
echo $PATH | grep /usr/bin

# Reinstall if necessary
sudo dpkg --configure nextor
```

#### Error: "Python import failed"

```bash
# Verify Python package installed correctly
dpkg -L nextor | grep -E '\.py$'

# Check package contents
dpkg -c ../nextor_1.1-1_all.deb | grep -E '\.py$'

# Verify Python path
python3 -c "import sys; print(sys.path)"

# Test imports manually
python3 -c "from Nex_Tor_IP_changer.NexTOR import main"
```

## Additional Commands

### Size Analysis

```bash
# Binary package size
du -h ../nextor_1.1-1_all.deb

# Uncompressed size
dpkg-deb -I ../nextor_1.1-1_all.deb | grep Installed-Size

# Breakdown by directory
dpkg-deb -x ../nextor_1.1-1_all.deb /tmp/analyze
du -sh /tmp/analyze/*/
```

### Compatibility Testing

```bash
# Test on different distributions
# Simulate Debian Bookworm
debootstrap bookworm /tmp/bookworm
chroot /tmp/bookworm /bin/bash
dpkg -i /nextor_1.1-1_all.deb

# Or use Docker for isolation
docker run -it debian:bookworm bash
apt-get update
dpkg -i /nextor_1.1-1_all.deb
```

### Security Checks

```bash
# Scan for vulnerabilities in dependencies
apt-cache depends --recurse nextor

# Verify GPG signature (if signed)
dpkg-sig --verify ../nextor_1.1-1_all.deb

# Check for suspicious permissions
dpkg-deb -x ../nextor_1.1-1_all.deb /tmp/sec
find /tmp/sec -type f -perm /006
```

## Final Checklist

Before submitting to Kali Linux:

- [ ] `debuild -us -uc` completes without errors
- [ ] Package file exists: `../nextor_1.1-1_all.deb`
- [ ] `lintian -i` shows no errors (only warnings/info)
- [ ] `sudo dpkg -i` installs successfully
- [ ] `nextor` command is executable
- [ ] `man nextor` displays properly
- [ ] `python3 -c "from Nex_Tor_IP_changer import NexTOR"` works
- [ ] Dependencies listed in `debian/control` are all required and available
- [ ] No Debian Policy violations
- [ ] Copyright file is complete and accurate
- [ ] Package builds on target distributions (Debian/Kali)
- [ ] All Python files have shebang header if executable

---

**For more information:**
- [DEBIAN_PACKAGING.md](DEBIAN_PACKAGING.md) - Detailed Debian packaging guide
- [KALI_SUBMISSION.md](KALI_SUBMISSION.md) - Kali Linux submission process
- [Debian Policy Manual](https://www.debian.org/doc/debian-policy/)
- [debhelper Documentation](https://manpages.debian.org/debhelper)
