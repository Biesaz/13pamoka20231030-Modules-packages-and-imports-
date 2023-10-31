
import win32api

def turn_off_secondary_monitor():
  """Turns off the secondary monitor."""

  # Get the monitor handles.
  monitor_handles = win32api.EnumDisplayMonitors()

  # Find the secondary monitor handle.
  secondary_monitor_handle = None
  for monitor_handle in monitor_handles:
    if monitor_handle != win32api.GetPrimaryMonitor():
      secondary_monitor_handle = monitor_handle
      break

  # If the secondary monitor handle is not None, turn off the monitor.
  if secondary_monitor_handle is not None:
    win32api.SetMonitorPowerState(secondary_monitor_handle, win32api.MONITOR_POWER_STATE_OFF)

# Turn off the secondary monitor.
turn_off_secondary_monitor()