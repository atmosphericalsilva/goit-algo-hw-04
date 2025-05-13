def get_cats_info(cat_path):

    try:
        # safely opening the file in the right format
        with open(cat_path, 'r', encoding = 'utf-8') as file:

            # separating the text into lines
            cats = file.readlines()

            cat_list = list()

            # separating and adding the data into dictionary
            for cat in cats:

                cat_dict = {
                    "id": cat.split(',')[0].strip(),
                    "name": cat.split(',')[1].strip(),
                    "age": cat.split(',')[2].strip()
                }

                # adding dictionaries into the list
                cat_list.append(cat_dict)

            return cat_list
        
    # handling incorrect file data
    except (UnicodeDecodeError, IndexError, ValueError) as e:
        print(f'failed to read file: {e}')