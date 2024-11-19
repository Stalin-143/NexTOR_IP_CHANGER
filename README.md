# Nex_Tor_IP_Changer v1.0

### Automatically Change Your IP Address Using the Tor Network

#### This tool leverages the Tor project to periodically change your IP address. It is ideal for privacy enthusiasts or anyone requiring dynamic IP rotation.
## Features:

  Automatically changes IP address via the Tor network.
  Simple installation and usage.
  Designed for Linux systems.

## Installation Instructions:

## Requirements:

  Install Tor:

    sudo apt install tor

## Install required Python libraries:

    pip3 install requests[socks]

  Alternatively, running the NexTor script will handle dependencies automatically.

## Steps:

  ### Clone the repository:

    git clone https://github.com/Stalin-143/NexTOR_IP_CHANGER

## Navigate to the project directory:

    cd Nex_Tor_IP_changer

## Run the installation script:

    python3 install.py

### After installation, you can use the command Nex from any terminal to start the tool.

## Usage:

  ### Run the command:

    Nex
    
## Follow the prompts:

  Enter the time interval (in seconds) for IP changes.
  Specify the number of IP changes (or set to infinite by entering 0).

  Set your browser or application to use the SOCKS proxy at 127.0.0.1:9050.

## Notes:

  The tool works on systems with Tor properly installed and running.
  Configure your application or browser to use the proxy settings for IP rotation:
      SOCKS Proxy: 127.0.0.1
      Port: 9050
  For infinite IP changes, enter 0 when prompted.

## Example:

  Launch the tool:

    Nex

  Set time to change IP (e.g., every 60 seconds).
  Set the number of changes (e.g., 10 or 0 for infinite changes).
  Open your browser and configure the SOCKS proxy to 127.0.0.1:9050.

### Enjoy enhanced privacy and dynamic IP rotation!

## Image:

## After Running

![Screenshot_2024-11-20_00_42_09](https://github.com/user-attachments/assets/4a18015f-4910-493e-9f3a-0fd8fbf31b2e)

## RESULT

![Screenshot_2024-11-20_00_17_27](https://github.com/user-attachments/assets/308df2a7-9a58-4b4e-a04d-0042d9fa7819)




## License:

This project is open source and distributed under the MIT License. Contributions are welcome!


