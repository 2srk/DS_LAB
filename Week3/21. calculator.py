{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a24adeb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "# Function to update the expression in the entry field\n",
    "def press(key):\n",
    "    entry_var.set(entry_var.get() + str(key))\n",
    "\n",
    "# Function to evaluate the expression\n",
    "def calculate():\n",
    "    try:\n",
    "        result = eval(entry_var.get())  # Evaluate expression\n",
    "        entry_var.set(result)  # Update entry field with result\n",
    "    except:\n",
    "        entry_var.set(\"Error\")  # Handle invalid input\n",
    "\n",
    "# Function to clear the entry field\n",
    "def clear():\n",
    "    entry_var.set(\"\")\n",
    "\n",
    "# Creating the main GUI window\n",
    "root = tk.Tk()\n",
    "root.title(\"Simple Calculator\")\n",
    "root.geometry(\"300x400\")\n",
    "\n",
    "# Entry widget to display the expression/result\n",
    "entry_var = tk.StringVar()\n",
    "entry = tk.Entry(root, textvariable=entry_var, font=(\"Arial\", 20), bd=5, justify=\"right\")\n",
    "entry.pack(fill=\"both\", ipadx=8, pady=10, padx=10)\n",
    "\n",
    "# Creating a frame for buttons\n",
    "button_frame = tk.Frame(root)\n",
    "button_frame.pack()\n",
    "\n",
    "# Button layout\n",
    "buttons = [\n",
    "    ('7', '8', '9', '/'),\n",
    "    ('4', '5', '6', '*'),\n",
    "    ('1', '2', '3', '-'),\n",
    "    ('C', '0', '=', '+')\n",
    "]\n",
    "\n",
    "# Adding buttons to the GUI\n",
    "for row in buttons:\n",
    "    row_frame = tk.Frame(button_frame)\n",
    "    row_frame.pack()\n",
    "    for char in row:\n",
    "        btn = tk.Button(row_frame, text=char, font=(\"Arial\", 15), width=5, height=2, command=lambda ch=char: press(ch) if ch not in ('=', 'C') else (calculate() if ch == '=' else clear()))\n",
    "        btn.pack(side=\"left\", padx=5, pady=5)\n",
    "\n",
    "# Run the application\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98687c5a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
