#!/usr/bin/env python3
import os
import sys

def check_reboot():
	"""Return True if their is any pending reboots."""
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print("Reboot Pending!")
		sys.exit(1)
	print("Everything is fine.")
	sys.exit(0)
main()


