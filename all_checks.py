#!/usr/bin/env python3
import os

def check_reboot():
	"""Return True if their is any pending reboots."""
	return os.path.path("/run/reboot-required")

def main():
	pass

main()


