import time

print("""

  +-------+ '++++++++++'  ++__-       |-  ++             ++  ||+=======   
  |+------+ |+        |+  |+  +-      |-   --           --   ||-  
  |+        |+        |+  |+   +-     |-    ++         ++    ||+   
  |+        |+        |+  |+    +-    |-     --       --     ||--------   
  |+        |+        |+  |+     +-   |-      ++     ++      ||++++++++
  |+        |+        |+  |+      +-  |-       --   --       ||-
  |+------+ |+        |+  |+       +- |-        ++ ++        ||+
  +-------+ '++++++++++'  |+        +-|-         ---         ||======== .rt
  
""")

print("Simple Converterter from m to cm, and vice versa.")
print("Project Convert!")

prompt = '> '

for i in range(3, 0, -1):
    i = '*'
    time.sleep(1)
    print(i)

# Choose one
print("Please choose one of the options:")

print("""
[1] Convert from m to cm
[2] Convert from cm to m
""")

# Input
answer = input(prompt)

# if/else for multiple choice
if answer == '1':
    print("Add values ...")
    m_to_cm = float(input(prompt))  # your input
    m_to_cm_data = float(m_to_cm*100)  # your input *100
    print(float(m_to_cm_data), "centimeters")  # final result
elif answer == '2':
    print("Add values ...")
    cm_to_m = float(input(prompt))
    cm_to_m_data = float(cm_to_m / 100)
    print(float(cm_to_m_data), "meters")
else:
    print("Invalid input.")
