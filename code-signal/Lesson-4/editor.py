class Editor:
  def __init__(self):
    self.text = ""
    self.history_stack = []
    self.redo_stack = []

  def append_text(self, text):
    self.history_stack.append(self.text)
    self.text += text

  def undo(self):
    if self.history_stack:
      self.redo_stack.append(self.text)
      self.text = self.history_stack.pop()
    else:
      print("Undo operation not possible. No history available.")

  def redo(self):
    if self.redo_stack:
      self.history_stack.append(self.text)
      self.text = self.redo_stack.pop()
    else:
      print("Redo operation not possible. No redo history available.")

  def display_text(self):
    print(self.text)


editor = Editor()

editor.append_text("Hello, ")
editor.append_text("CodeSignal!")
editor.display_text()
editor.undo()
editor.display_text()
editor.undo()
editor.display_text()
editor.redo()
editor.display_text()
editor.redo()
editor.display_text()
editor.redo()
editor.undo()


class History:
  def __init__(self):
    self.history_stack = []
    self.future_stack = []

  def execute_action(self, action):
    self.history_stack.append(action)
    print(f"Executing: {action}")

  def undo_action(self):
    if self.history_stack:
      self.future_stack.append(self.history_stack.pop())
      action = self.history_stack[-1]
      print(f"Undid, now on action: {action}")
    else:
      print("Nothing to undo. Initialize a new action first.")

  def redo_action(self):
    if self.future_stack:
      action = self.future_stack.pop()
      self.history_stack.append(action)
      print(f"Redid, now on action: {action}")
    else:
      print("Nothing to redo")

history = History()
history.undo_action()

class Copy_Paste:
  def __init__(self):
    self.clipboard = []
    self.history = []
    self.text = ""

  def copy(self, text):
    self.clipboard.append(text)

  def paste(self):
    if self.text:
      self.text += ", " + "".join(self.clipboard)
    else:
      self.text += "".join(self.clipboard)

  def cut(self, text):
    self.copy(text)
    self.text = self.text.replace(text, "", 1)

  def undo(self):
    if self.history:
      self.text = self.history.pop()
    else:
      print("Nothing to undo.")
  
  def add_text(self, text):
    self.history.append(self.text)
    self.text += text

  def display_text(self):
    print(self.text)

copy_paste = Copy_Paste()
copy_paste.add_text("Hello, ")
copy_paste.add_text("World!")
copy_paste.display_text()
copy_paste.copy("World!")
copy_paste.paste()
copy_paste.display_text()
copy_paste.cut("World!")
copy_paste.display_text() 