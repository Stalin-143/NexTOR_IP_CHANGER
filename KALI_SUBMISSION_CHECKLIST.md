# Kali Linux Package Submission Checklist

Last Updated: 14 Apr 2026  
Project: NexTOR IP Changer  
Version: 1.1  
Maintainer: Stalin

---

## ✅ Pre-Submission Requirements

### Local Setup
- [ ] Install required tools:
  ```bash
  sudo apt-get install -y git git-buildpackage debhelper devscripts \
    pristine-tar build-essential dh-python python3-setuptools lintian \
    gnupg
  ```

- [ ] Generate/verify GPG key:
  ```bash
  gpg --list-keys
  # If no key exists:
  gpg --gen-key
  ```

- [ ] Configure git (if not done):
  ```bash
  git config --global user.name "Stalin"
  git config --global user.email "stalin@example.com"
  git config --global user.signingkey <YOUR_KEY_ID>
  ```

### Package Files Updated
- [x] `debian/control` - Updated with Kali VCS fields
- [x] `debian/changelog` - Added Kali 1.1-1kali1 entry
- [x] `debian/README.Debian` - Created with Debian-specific docs
- [x] `.gitlab-ci.yml` - Created for Kali CI/CD
- [x] `.git-buildpackagerc` - Created for gbp configuration

---

## 📋 Current Status

### Completed ✅
- GitLab repository published: https://gitlab.com/5t4l1n/NexTOR_IP_CHANGER.git
- Debian package files properly structured
- Kali metadata added to debian/control
- CI/CD pipeline configured

### Next Steps 👉
1. Create Kali account + request repo access
2. Test local package build
3. Fork Kali repo or contact Kali team
4. Submit merge request or formal request

---

## 🔧 Build & Test Locally (BEFORE SUBMISSION)

### Test Build Package
```bash
cd /home/w4nn4d13/Downloads/nextor-1.1

# Build the package
gbp buildpackage --git-ignore-new -us -uc

# Check for lintian errors
lintian -i nextor_1.1-1kali1_all.deb
```

### Install & Test
```bash
# Install the built package
sudo apt-get install ./nextor_1.1-1kali1_all.deb

# Verify installation
nextor --help

# Check dependencies
dpkg -l | grep -E 'tor|python3-stem|python3-requests'
```

---

## 🚀 Kali Submission Process

### Option 1: Submit via Kali Merge Request (Recommended)

1. **Create Kali GitLab Account**
   - Visit: https://gitlab.com/users/sign_up
   - Verify email

2. **Request Kali Package Maintainer Access**
   - Visit: https://kali.org/community/
   - Fill out package maintainer request form
   - OR contact: devel@kali.org

3. **Fork/Create in Kali Repository**
   ```bash
   # Once you have access, fork:
   # https://gitlab.com/kali-team/packages/
   
   # Clone to local
   git clone https://gitlab.com/YOUR_USERNAME/nextor.git
   cd nextor
   ```

4. **Add Upstream Remote**
   ```bash
   git remote add upstream https://gitlab.com/5t4l1n/NexTOR_IP_CHANGER.git
   git fetch upstream
   ```

5. **Prepare for Merge Request**
   ```bash
   # Create feature branch
   git checkout -b add-nextor-package
   
   # Copy your debian files
   cp -r /path/to/nextor-1.1/debian ./
   cp /path/to/nextor-1.1/.gitlab-ci.yml ./
   cp /path/to/nextor-1.1/.git-buildpackagerc ./
   
   # Commit with signature
   git add debian/ .gitlab-ci.yml .git-buildpackagerc
   git commit -S -m "Add NexTOR IP Changer package for Kali Linux"
   
   # Push to your fork
   git push origin add-nextor-package
   ```

6. **Submit Merge Request**
   - Visit your forked repo on GitLab
   - Click "Merge Requests" → "New Merge Request"
   - Target: `kali-team/packages/nextor:master`
   - Fill in description:
     ```
     **Package:** NexTOR IP Changer
     **Version:** 1.1-1kali1
     **Upstream:** https://gitlab.com/5t4l1n/NexTOR_IP_CHANGER.git
     **Description:** 
     Tor exit node IP address rotator for privacy and security testing
     
     **Features:**
     - Automatic IP rotation via Tor
     - SOCKS5 proxy integration
     - Command-line interface
     - Lightweight and efficient
     
     **Dependencies properly declared:** ✓
     **Lintian checks pass:** ✓
     **CI/CD pipeline configured:** ✓
     **README.Debian provided:** ✓
     ```

7. **Wait for Review**
   - Kali maintainers will review
   - They may request changes
   - Address feedback and push updates

---

### Option 2: Direct Contact with Kali Team

Send professional email to: **devel@kali.org**

Subject: `[PACKAGE REQUEST] NexTOR IP Changer - Tor IP Rotation Tool`

Body:
```
Dear Kali Linux Development Team,

I would like to submit a new package for inclusion in the Kali Linux repository:

Package Name: nextor
Version: 1.1-1kali1
Upstream: https://gitlab.com/5t4l1n/NexTOR_IP_CHANGER.git
Description: Automated Tor exit node IP rotator for privacy/security testing

The package includes:
- Complete Debian packaging files
- CI/CD pipeline (.gitlab-ci.yml)
- Comprehensive documentation
- All dependencies properly declared
- Lintian compliance verified

Repository: https://gitlab.com/5t4l1n/NexTOR_IP_CHANGER.git

I'm ready to contribute and maintain this package.

Best regards,
Stalin
```

---

## ✅ Pre-Submission Quality Checklist

Before submitting, verify:

### Code Quality
- [ ] No syntax errors: `python3 -m py_compile Nex_Tor_IP_changer/*.py`
- [ ] Proper Python 3.6+ compatibility
- [ ] All imports available in Debian repos

### Debian Standards
- [ ] `debian/control` - Proper format and Kali VCS fields
- [ ] `debian/changelog` - Properly formatted entry
- [ ] `debian/copyright` - Correct license information
- [ ] `debian/rules` - Proper permissions
- [ ] `debian/README.Debian` - Documentation provided
- [ ] No lintian errors: `lintian -i nextor_*.deb`

### Dependencies
- [ ] `tor` - Available in Kali
- [ ] `python3-requests` - Available in Kali
- [ ] `python3-stem` - Available in Kali
- [ ] No proprietary dependencies

### Documentation
- [ ] README.md - Clear and comprehensive
- [ ] Man page (nextor.1) - Properly formatted
- [ ] LICENSE - MIT license included
- [ ] MANIFEST.in - Correct file listing

### Security
- [ ] No sudo hardcoded
- [ ] Proper file permissions
- [ ] No credentials in source code
- [ ] No deprecated security libraries

---

## 📞 Kali Linux Resources

- **Kali Forum**: https://forums.kali.org/
- **Kali Documentation**: https://docs.kali.org/
- **Kali GitLab**: https://gitlab.com/kali-team/
- **Package Policy**: https://www.kali.org/tools/
- **Debian Policy**: https://www.debian.org/doc/debian-policy/

---

## 🎯 After Acceptance

Once your package is accepted:

1. **Package Published**
   - Will appear in: `apt-cache search nextor`
   - Available for: `apt-get install nextor`
   - Listed on: https://www.kali.org/tools/

2. **Maintenance**
   - Monitor for bug reports
   - Keep dependencies updated
   - Respond to security issues
   - Submit updates through Kali

3. **Version Updates**
   - Tag releases: `git tag v1.x`
   - Update `debian/changelog`
   - Resubmit through MR process

---

## 📊 Submission Timeline

Typical timeline:
- Package submission: Day 0
- Initial review: 2-5 business days
- Possible requests for changes: +2-3 days
- Final approval: +1-2 days
- Package in repos: Usually within 1 week

---

## ❓ FAQ

**Q: Do I need Kali Linux installed?**  
A: Not required, but recommended for testing. Use Docker/VM with Debian Bullseye.

**Q: Can I update the package after submission?**  
A: Yes, increment the version and resubmit as new MR.

**Q: What if Kali team requests changes?**  
A: They'll comment in the MR; make changes and push to same branch.

**Q: How long is maintenance required?**  
A: Indefinitely, but you can step down if needed (hand off to another maintainer).

**Q: What about security vulnerabilities?**  
A: You should report/fix them promptly and submit updates.

---

## 🎉 Good Luck!

Your package looks solid. Follow these steps and it should be accepted smoothly.

For questions: Contact Kali development team or visit the forums.

**Last checked:** 14 Apr 2026
