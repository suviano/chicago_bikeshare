def column_to_list_lazy(data, index):
    """
    generator with a specific index of a list inside another list
      Args:
          data: the data from the csv with an list for each line and the value is also a list.
          index: the index for the column to be returned.
      Returns:
          yield a index specified from the input
    """
    for line in data:
        yield line[index]

def column_to_list(data, index):
    """
    return the list of an column.
      Args:
          data: the data from the csv with an list for each line and the value is also a list.
          index: the index for the column to be returned.
      Returns:
          return only the column specified from the input
    """
    # Tip: You can use a for to iterate over the samples,
    # get the feature by index and append into a list
    return [col_item[index] for col_item in data]