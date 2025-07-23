# NexTor IP Changer v1.0

🕵️‍♂️ **Automatically Change Your IP Address Using the Tor Network**

NexTor IP Changer is a lightweight, command-line tool designed to enhance online privacy by leveraging the Tor network to periodically rotate your IP address. This tool is perfect for privacy enthusiasts, security researchers, or anyone requiring dynamic IP rotation for legitimate purposes, such as testing network configurations or maintaining anonymity.

🚀 **Features**

- **Automated IP Rotation**: Seamlessly changes your IP address using the Tor network at user-defined intervals.
- **Simple Command-Line Interface**: Run the tool with a single command (`nextor`) and follow intuitive prompts.
- **Lightweight and Efficient**: Minimal resource usage, optimized for Arch Linux systems.
- **Flexible Configuration**: Set custom time intervals and the number of IP changes, including an option for infinite rotation.
- **Application Integration**: Works with any application or browser that supports SOCKS proxy settings.
- **Arch Linux Support**: Available in the Arch User Repository (AUR) for easy installation.

🛠️ **Installation (Arch Linux Only)**

📦 **Requirements**

Before using NexTor IP Changer, ensure the following dependencies are installed and configured:

1. **Tor**: The tool relies on the Tor network for IP rotation.
   ```bash
   sudo pacman -S tor
   sudo systemctl enable --now tor
   ```

2. **Python Libraries**: The `requests[socks]` library is required for proxy communication.
   ```bash
   pip3 install requests[socks]
   ```

🔧 **Verify Tor is Running**

Ensure the Tor service is active before running the tool:
```bash
sudo systemctl status tor
```
If Tor is not running, start it with:
```bash
sudo systemctl start tor
```

📦 **Install from AUR**

The easiest way to install NexTor IP Changer is through the Arch User Repository (AUR) using an AUR helper like `yay`:
```bash
yay -S nextor-ip-changer
```

This installs the tool system-wide, allowing you to run it with the `nextor` command:
```bash
nextor
```

📦 **Install from Source**

For users who prefer manual installation or want to customize the tool:

1. Clone the repository:
   ```bash
   git clone https://github.com/Stalin-143/NexTOR_IP_CHANGER
   ```

2. Navigate to the project directory:
   ```bash
   cd NexTOR_IP_CHANGER
   ```

3. Run the installation script:
   ```bash
   python3 install.py
   ```

After installation, the `nextor` command will be available globally.

🧪 **Usage**

Launch the tool by running:
```bash
nextor
```

The tool will prompt you to:
- **Enter the time interval** (in seconds) between IP changes (e.g., `60` for every minute).
- **Specify the number of IP changes** (e.g., `10` for ten rotations, or `0` for infinite changes).

🔌 **Proxy Configuration**

To route your traffic through the Tor network and benefit from IP rotation, configure your application or browser to use the following SOCKS proxy settings:
- **Host**: `127.0.0.1`
- **Port**: `9050`

For example, in Firefox:
1. Go to **Settings > General > Network Settings**.
2. Select **Manual proxy configuration**.
3. Set **SOCKS Host** to `127.0.0.1` and **Port** to `9050`.
4. Enable **SOCKS v5** and save.

This ensures your traffic is routed through Tor with rotating IPs as configured by the tool.

🔔 **Notes**

- **Verify Tor Status**: Always confirm that the Tor service is running before using the tool (`sudo systemctl status tor`).
- **Infinite Rotation**: Enter `0` when prompted for the number of changes to enable continuous IP rotation.
- **Arch Linux Optimization**: The tool is specifically packaged for Arch Linux via the AUR, ensuring seamless integration.
- **Proxy Settings**: Incorrect proxy configurations in your application or browser may prevent IP rotation. Double-check the settings if issues arise.
- **Performance**: The tool is designed to be lightweight, but frequent IP changes may impact network performance depending on your connection.

🌟 **Contributing**

We welcome contributions from the community to improve NexTor IP Changer! Here’s how you can get involved:

- **Bug Reports**: Found a bug? Open an issue on the [GitHub Issues page](https://github.com/Stalin-143/NexTOR_IP_CHANGER/issues) with a detailed description, including steps to reproduce and your system details.
- **Feature Requests**: Have an idea for a new feature? Submit a feature request via GitHub Issues, explaining how it would enhance the tool.
- **Pull Requests**: Want to contribute code? Follow these steps:
  1. Fork the repository.
  2. Create a new branch (`git checkout -b feature/your-feature-name`).
  3. Make your changes and commit them with clear messages (`git commit -m "Add your feature description"`).
  4. Push to your fork (`git push origin feature/your-feature-name`).
  5. Open a pull request on the [GitHub repository](https://github.com/Stalin-143/NexTOR_IP_CHANGER).
- **Code Style**: Follow Python PEP 8 guidelines for code contributions. Ensure your code is well-documented and includes appropriate comments.
- **Testing**: Test your changes thoroughly on an Arch Linux system with Tor installed to ensure compatibility.

📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

⚠️ **Disclaimer**

This script is provided "as is" without any warranties or guarantees. The author is not responsible for any misuse or unintended consequences that may arise from using this script. Please use it responsibly and in compliance with your local laws and network policies.

💰 **Support the Project**

If you find NexTor IP Changer useful, consider supporting its development:  
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/stalin143)  
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/stalinS143)

📬 **Contact**

For questions, feedback, or support, reach out via the [GitHub Issues page](https://github.com/Stalin-143/NexTOR_IP_CHANGER/issues). You can also connect with the community through discussions on the repository.



  



