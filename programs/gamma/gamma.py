import tkinter as tk
from heuslertools.squid.gamma import gamma

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Gamma calculator")

    length_label = tk.Label(window, text='Sample length (mm):', font=("Arial Bold", 20))
    length_label.grid(column=0, row=0)
    length_input = tk.Entry(window, width=5, font=("Arial Bold", 20))
    length_input.grid(column=1, row=0)

    width_label = tk.Label(window, text='Sample width (mm):', font=("Arial Bold", 20))
    width_label.grid(column=0, row=1)
    width_input = tk.Entry(window, width=5, font=("Arial Bold", 20))
    width_input.grid(column=1, row=1)

    output_label = tk.Label(window, text='Gamma:', font=("Arial Bold", 20))
    output_label.grid(column=0, row=2)
    output = tk.Label(window, text='', font=("Arial Bold", 20))
    output.grid(column=1, row=2)

    def calculate():
        try:
            length = float(length_input.get())
            width = float(width_input.get())
            output.configure(text=str(round(gamma(length*1e-3, width*1e-3), 4)))
        except Exception as e:
            print(e)

    calc_btn = tk.Button(window, text='Calculate', font=("Arial Bold", 20), command=calculate)
    calc_btn.grid(column=0, row=3)

    window.mainloop()
