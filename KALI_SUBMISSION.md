# Kali Linux Package Submission Guide

This guide explains how to submit the NexTOR IP Changer package to the official Kali Linux repository.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Kali Linux Packaging Standards](#kali-linux-packaging-standards)
3. [Repository Structure](#repository-structure)
4. [GitLab Setup](#gitlab-setup)
5. [Package Submission Process](#package-submission-process)
6. [Merge Request Guidelines](#merge-request-guidelines)
7. [After Acceptance](#after-acceptance)

## Prerequisites

### Required Accounts and Tools

1. **Kali Linux GitLab Account**
   - Register at https://gitlab.com/
   - Join the Kali Linux organization
   - Request maintainer access

2. **GPG Key Setup** (for signing packages)
   
   ```bash
   # Generate GPG key if you don't have one
   gpg --gen-key
   
   # List your keys
   gpg --list-keys
   
   # Configure git to use your key
   git config --global user.signingkey <KEY_ID>
   ```

3. **Git Tools**
   
   ```bash
   sudo apt-get install -y \
       git \
       Git-buildpackage \
       debhelper \
       devscripts \
       pristine-tar
   ```

4. **Debian Build Tools**
   
   ```bash
   sudo apt-get install -y \
       build-essential \
       dh-python \
       python3-setuptools \
       lintian
   ```

## Kali Linux Packaging Standards

### Package Naming Conventions

**Kali Repository Structure:**
```
kali-tools/packages/
└── nextor/
    ├── debian/
    │   └── (all debian files)
    ├── Nex_Tor_IP_changer/
    ├── upstream/
    │   └── (tracks upstream source)
    ├── .git-buildpackagerc
    └── README
```

### Mandatory Changes for Kali

1. **Adjust Maintainer Field**
   
   In `debian/control`, change to:
   
   ```
   Maintainer: Kali Linux <devel@kali.org>
   Uploaders: Stalin <stalin@example.com>
   ```

2. **Add Kali-Specific Section**
   
   In `debian/control`:
   
   ```
   Homepage: https://github.com/Stalin-143/NexTOR_IP_CHANGER
   Vcs-Git: https://gitlab.com/kali-team/packages/nextor.git
   Vcs-Browser: https://gitlab.com/kali-team/packages/nextor
   ```

3. **Update Changelog Entry**
   
   In `debian/changelog`:
   
   ```
   nextor (1.1-1kali1) kali-dev; urgency=high
   
     * Kali Linux package release
     * Automated Tor exit node rotation
   
    -- Kali Linux <devel@kali.org>  Mon, 14 Apr 2026 00:00:00 +0000
   ```

4. **Add Package Metadata**
   
   Create `debian/README.Debian`:
   
   ```
   NexTOR IP Changer for Debian
   
   Installation:
     apt-get install nextor
   
   Usage:
     nextor
   
   Documentation:
     man nextor
   
   Upstream: https://github.com/Stalin-143/NexTOR_IP_CHANGER
   ```

### Compliance Checklist

- [ ] No proprietary code or non-open-source dependencies
- [ ] Clean lintian report
- [ ] Proper copyright headers
- [ ] MIT License compatible with Debian
- [ ] No security vulnerabilities in dependencies
- [ ] Package builds on all supported Debian releases
- [ ] Binary package is reproducible
- [ ] Documentation is complete

## Repository Structure

### Kali Packages Repository

Kali Linux maintains packages in a structured GitLab repository:

```
https://gitlab.com/kali-team/packages/
```

Each package has its own repository:

```
https://gitlab.com/kali-team/packages/nextor/
```

### Repository Organization

```
nextor/
├── .git/              # Git repository
├── .gitlab-ci.yml     # CI/CD pipeline configuration
├── debian/            # Debian packaging files
├── upstream/          # Upstream source tracking (pristine-tar)
├── .git-buildpackagerc
├── README
└── docs/              # Additional documentation
```

## GitLab Setup

### Fork the Repository

1. Visit https://gitlab.com/kali-team/packages
2. Fork the organization (request access first)
3. Clone the kali-tools repository

   ```bash
   git clone https://gitlab.com/kali-team/packages/nextor.git
   cd nextor
   ```

### Configure Git

```bash
# Set user information
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Set signing key
git config user.signingkey <GPG_KEY_ID>

# Enable auto-signing
git config commit.gpgsign true
```

### Create Remote Tracking

```bash
# Add upstream
git remote add upstream https://gitlab.com/kali-team/packages/nextor.git

# Verify remotes
git remote -v
```

## Package Submission Process

### Step 1: Prepare the Repository

```bash
# Create working directory
mkdir -p ~/kali-packages
cd ~/kali-packages

# Clone or initialize
git clone https://gitlab.com/<your-username>/packages/nextor.git
cd nextor

# If new repo, copy files
cp -r /path/to/NexTOR_IP_CHANGER/* .
```

### Step 2: Update Packaging Files

Update files for Kali compliance:

```bash
# Edit maintainer information
nano debian/control

# Update version for Kali
nano debian/changelog

# Add Kali-specific documentation
cat > debian/README.Debian << 'EOF'
NexTOR IP Changer for Kali Linux

This package provides automated Tor exit node rotation for privacy
research, OSINT, and security testing.

Installation:
  sudo apt-get install nextor

Usage:
  nextor

Requirements:
  - Tor daemon must be running
  - Python 3.6+

See man page for detailed usage:
  man nextor

Security:
  This tool is for ethical use only. Ensure compliance with all
  applicable laws and terms of service.
EOF
```

### Step 3: Build and Test

```bash
# Install build dependencies
sudo apt-get build-dep .

# Build the package
debuild -us -uc

# Run lintian
lintian -i ../nextor_*.deb

# Test installation
sudo dpkg -i ../nextor_*.deb
```

### Step 4: Commit Changes

```bash
# Stage all changes
git add debian/ .gitignore MANIFEST.in pyproject.toml setup.py

# Create signed commit
git commit -S -m "Initial Kali Linux package for nextor 1.1"

# Verify commit is signed
git log --show-signature
```

### Step 5: Push to GitLab

```bash
# Push to your fork
git push -u origin main

# Or to specific branch for merge request
git checkout -b submit/nextor-1.1
git push -u origin submit/nextor-1.1
```

### Step 6: Create Merge Request

1. Visit your forked repository on GitLab
2. Click "Create merge request"
3. Target: `kali-team/packages/nextor:master`
4. Source: Your feature branch

**Merge Request Template:**

```markdown
## Summary
Initial Debian package for NexTOR IP Changer v1.1

## Description
NexTOR IP Changer is a command-line tool for rotating Tor exit nodes
and dynamically changing your public IP address. Designed for privacy
research, OSINT, and security testing.

## Checklist
- [x] Builds cleanly
- [x] Lintian report clean
- [x] Dependencies correct
- [x] Copyright file complete
- [x] Man page included
- [x] Tested on Debian/Kali
- [x] License compliant (MIT)

## Testing
```bash
debuild -us -uc
lintian -i ../nextor_*.deb
sudo dpkg -i ../nextor_*.deb
nextor --help
man nextor
```

## References
- GitHub: https://github.com/Stalin-143/NexTOR_IP_CHANGER
- License: MIT
- Upstream Version: 1.1
```

## Merge Request Guidelines

### Automated CI/CD Checks

Kali Linux enforces automated checks:

1. **Lintian Scan**
   - Zero errors allowed
   - Warnings reviewed case-by-case

2. **Build Test**
   - Package must build on:
     - Debian Bookworm
     - Debian Testing
     - Debian Unstable

3. **GPG Signature**
   - All commits must be signed
   - Maintainer key must be verified

### Code Review Process

- **Timeline:** 2-7 business days
- **Reviewers:** Kali Linux maintainers
- **Feedback:** Via GitLab merge request comments
- **Iterations:** Expected to address feedback

### Common Feedback Points

| Issue | Resolution |
|-------|-----------|
| Inconsistent formatting | Follow Debian policy strictly |
| Missing dependencies | Add to debian/control Depends |
| Lintian warnings | Document or fix per warning |
| Upstream source issues | Link to upstream security policy |
| Documentation gaps | Enhance README.Debian |

## After Acceptance

### Upon Merge Approval

1. **Automatic Actions**
   - Package submitted to build system
   - Build artifacts created for all supported releases
   - Package added to testing repository

2. **Verification**
   
   ```bash
   # Check package in Kali repository
   apt-cache search nextor
   apt-cache show nextor
   
   # Install from official repository
   sudo apt-get update
   sudo apt-get install nextor
   ```

3. **Version Management**
   
   - Maintain package in Kali repository
   - Update debian/changelog for new versions
   - Follow Kali release schedule
   - Respond to security advisories

### Maintaining the Package

```bash
# Regular updates
git pull upstream master
git checkout -b update/nextor-1.2
# Make changes
git add debian/changelog debian/control ...
git commit -S -m "Update nextor to 1.2"
git push -u origin update/nextor-1.2
# Create merge request
```

## Contact and Support

### Kali Linux Resources

- **Main Website:** https://www.kali.org/
- **GitLab:** https://gitlab.com/kali-team/
- **Documentation:** https://www.kali.org/docs/
- **Mailing List:** devel@kali.org
- **IRC:** #kali-linux on Libera.Chat

### Package Maintainer Contact

For questions about this specific package:
- Email: stalin@example.com
- GitHub: https://github.com/Stalin-143/

## Submission Timeline Example

```
Day 1:   Prepare package, run local tests
Day 2:   Push to GitLab, create merge request
Day 3-5: Code review, address feedback
Day 6:   Approval and merge
Day 7+:  Appears in Kali testing repository
```

## Quick Reference Commands

```bash
# Clone repository
git clone https://gitlab.com/kali-team/packages/nextor.git

# Build package
debuild -us -uc

# Test package
lintian ../nextor_*.deb
sudo dpkg -i ../nextor_*.deb

# Commit with signature
git commit -S -m "message"

# Push changes
git push origin branch-name

# View merge requests
git log --graph --all --decorate
```

## Security Considerations for Submission

1. **Dependency Audit**
   ```bash
   # Check package dependency tree
   apt-cache depends nextor
   
   # Verify versions
   apt-cache policy python3-stem python3-requests
   ```

2. **Vulnerability Scanning**
   ```bash
   # Check for known CVEs
   apt-cache policy tor python3-stem
   ```

3. **License Verification**
   - All dependencies must have compatible licenses
   - MIT is fully compatible with Debian
   - Document any license interactions

## Appendix: Template Files

### debian/control (Kali Version)

```
Source: nextor
Maintainer: Kali Linux <devel@kali.org>
Uploaders: Stalin <stalin@example.com>
Section: utils
Priority: optional
Standards-Version: 4.6.1
Homepage: https://github.com/Stalin-143/NexTOR_IP_CHANGER
Vcs-Git: https://gitlab.com/kali-team/packages/nextor.git
Vcs-Browser: https://gitlab.com/kali-team/packages/nextor
Build-Depends: debhelper-compat (= 13),
               dh-python,
               python3-setuptools,
               python3-all
Rules-Requires-Root: no

Package: nextor
Architecture: all
Depends: ${python3:Depends},
         ${misc:Depends},
         python3,
         python3-requests,
         python3-stem,
         tor
Recommends: python3-pip,
            curl,
            wget
Description: Tor exit node IP address rotator
 NexTOR IP Changer is a command-line tool for automatically rotating
 your IP address using the Tor network. Ideal for privacy research,
 OSINT, and security testing.
```

### .gitlab-ci.yml (Kali CI/CD)

```yaml
stages:
  - build
  - test
  - sign

variables:
  DEBUILD_OPTS: "-us -uc"

build_package:
  stage: build
  script:
    - debuild $DEBUILD_OPTS
  artifacts:
    paths:
      - "../nextor_*.deb"

lintian_check:
  stage: test
  script:
    - lintian -i "../nextor_*.deb"

gpg_check:
  stage: sign
  script:
    - git log --show-signature HEAD
```
