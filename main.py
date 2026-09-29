from delete_el_id import delete_id


id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def commands(arr: list[int]):
  print("Выбирете команду: 1) Удалить элемент из массива, 2)Добавить элемент в массив")
  command = int(input())

  if command == 1:
    print(f"Введите элемент массива, который хотите удалить {len(arr)}")
    index = int(input())

    delete_id(arr, index)
    print(f"Элемент успешно удален, ваш массив: {arr}")


commands(arr=id_list)
