import prod_and_random
import create

def test_create():
    create_data = create.CreateData()
    create_data.create_date("date", "product","2023/02/01", "2023/02/25", 1)
    create_data.create_link_date("enddate", "date", 1, 30)
    create_data.create_datetime("datetime", "product", "2023/02/25 00:00:00", "2023/02/25 10:00:00", 60 * 60)
    create_data.create_link_datetime("enddatetime", "datetime", 1, 59)
    # create_data.create_amount("number", "random", 1, 112, 4)
    create_data.output_json("./output/input_sample_generated.json")

def test_prod_and_random():
    # json_file = "./input/input_sample_noProduct.json"
    # json_file = "./input/input_sample_noRandom.json"
    # json_file = "./input/input_sample4.json"
    json_file = "./output/input_sample_generated.json"
    output_path = "./output"

    print(json_file, output_path)
    
    dummydata_generator = prod_and_random.DummyDataGenerator(json_file)
    dummydata_generator.make_product_data()
    dummydata_generator.make_random_data()
    # dummydata_generator.output_csv(output_path)
    print(dummydata_generator.df)


if __name__ == "__main__" :
    test_create()
    # test_prod_and_random()
    
