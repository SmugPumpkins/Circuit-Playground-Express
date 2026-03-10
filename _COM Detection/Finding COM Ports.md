# Finding COM Ports

The two Python scripts provided, `COM_macos.py` and `COM_windows.py` are intended to help locate COM Ports to make it easier to identify where your Circuit Playground Express is located.

Once in a while, the scripts will fail. If this is the case, you can paste the following into your PyCharm terminal and it should provide a list of USB COM ports.
```
Get-CimInstance Win32_PnPEntity | Where-Object { $_.Name -like '*USB* (COM*' } | Select-Object -ExpandProperty Name
```