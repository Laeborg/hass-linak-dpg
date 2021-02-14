"""
Wrapper for bluetoothctl
"""

import time
import pexpect
import sys

class BTctl:
    """A wrapper for bluetoothctl utility."""

    def __init__(self):
        """Initalize shell."""
        self.process = pexpect.spawnu("bluetoothctl", echo=False)
        
    def convertHexStr(self, hexStr):
        """Convert Hex string to human readable."""
        value = int(hexStr[0:2], 16) + (int(hexStr[3:5], 16) << 8)
        
        if ((value&0x8000) == 0x8000):
            value = -((value^0xffff) + 1)
            
        return value
        
    def run(self, command, expectations=[], timeout=1):
        """Run command in shell."""
        self.process.send(f"{command}\n")
        time.sleep(timeout)
        
        expectations.append(pexpect.EOF)
        
        result = self.process.expect_exact(expectations, 3)
        if result == len(expectations) - 1:
            raise Exception(f"Unexpected response")
        
        return result
        
    def get_output(self, command, expectations=[], timeout=1):
        """Run command and get output from shell."""
        result = self.run(command, expectations, timeout)
        
        if result != 0:
            raise Exception(f"Failed to receive info.")
        
        if self.process.before:
            output = self.process.before.strip()
        else:
            output = ""
            
        return self.clean_output(output)
        
    def clean_output(self, input):
        """Remove unwanted characters from output."""
        formatting = [
            "\x1b[?2004h\x1b",
            "\x1b[0m",
            "\x1b[?2004l",
            "[0;94m",
            "\n"
        ]
        
        for format in formatting:
            input = input.replace(format, "")
            
        output = []
        
        for substring in input.split("\r"):
            output.append(substring.strip())
        
        return output
        
    def scan_start(self):
        """Start scanning for devices."""
        try:
            result = self.run(
                "scan on",
                [
                    "Discovery started"
                ],
                5
            )
            
            if result != 0:
                raise Exception(f"Failed to start scanning")

        except Exception as e:
            raise Exception(e)

        else:
            return True
            
    def scan_stop(self):
        """Stop scanning for devices."""
        try:
            result = self.run(
                "scan off",
                [
                    "Discovery stopped"
                ]
            )
            
            if result != 0:
                raise Exception(f"Failed to stop scanning")

        except Exception as e:
            raise Exception(e)

        else:
            return True
            
    def device_info(self, mac_address):
        """Get device info."""
        try:
            result = self.run(
                f"info {mac_address}",
                [
                    "Name:",
                    "not available"
                ]
            )
            
            if result != 0:
                raise Exception(f"Failed to receive device info")

        except Exception as e:
            raise Exception(e)

        else:
            return True
        
    def pair(self, mac_address):
        """Try to pair device."""
        try:
            result = self.run(
                f"pair {mac_address}",
                [
                    "Pairing successful",
                    "Failed to pair"
                ],
                5
            )
            
            if result != 0:
                raise Exception(f"Failed to pair device")

        except Exception as e:
            raise Exception(e)

        else:
            return True
        
    def connect(self, mac_address):
        """Try to connect to device."""
        try:
            result = self.run(
                f"connect {mac_address}",
                [
                    "Connection successful",
                    "Failed to connect",
                    "not available"
                ],
                3
            )
            
            if result != 0:
                raise Exception(f"Failed to establish connection")

        except Exception as e:
            raise Exception(e)

        else:
            return True
            
    def gatt(self):
        """Try to enter Generic Attribute mode."""
        try:
            result = self.run(
                "menu gatt",
                [
                    "Print environment variables",
                    "Invalid command"
                ]
            )
            
            if result != 0:
                raise Exception(f"Failed to enter Generic Attribute mode.")

        except Exception as e:
            raise Exception(e)

        else:
            return True
            
    def menu(self):
        """Try to enter default mode."""
        try:
            result = self.run(
                "back",
                [
                    "Print environment variables",
                    "Invalid command"
                ]
            )
            
            if result != 0:
                raise Exception(f"Failed to enter default mode.")

        except Exception as e:
            raise Exception(e)

        else:
            return True
            
    def attribute_info(self, uuid):
        """Try to get attribute info."""
        try:
            result = self.get_output(
                f"attribute-info {uuid}",
                [
                    "Flags:"
                ]
            )

        except Exception as e:
            raise Exception(e)

        else:
            return result
            
    def attribute_read_value(self, uuid):
        """Try to read value from attribute."""
        try:
            self.run(
                f"select-attribute {uuid}",
                [
                    ":/service"
                ]
            )
            
            result = self.get_output(
                "read",
                [
                    "..."
                ]
            )

        except Exception as e:
            raise Exception(e)

        else:
            return result