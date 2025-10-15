def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        ract_area = length * width
        return ract_area

    def perimeter():
        rect_perim = 2 * (length + width)
        return rect_perim

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"
