from collections import defaultdict


def main(from_currency, to_currency, cur_value):
    currencies = "AUD:USD:0.75,USD:CAD:1.26,USD:JPY:109.28,GBP:JPY:150.15"
    currencies_list = currencies.split(",")
    currency_map = defaultdict(list)

    for i in currencies_list:
        mappings = i.split(":")
        if mappings[0] in currency_map:
            currency_map[mappings[0]].append((mappings[1], float(mappings[2])))
        else:
            currency_map[mappings[0]] = [(mappings[1], float(mappings[2]))]

        if mappings[1] in currency_map:
            currency_map[mappings[1]].append((mappings[0], 1 / float(mappings[2])))
        else:
            currency_map[mappings[1]] = [(mappings[0], 1 / float(mappings[2]))]

    # print(currency_map)


    if from_currency in currency_map:
        available_exchanges = []
        for i in currency_map[from_currency]:
            if i[0] == to_currency:
                if cur_value:
                    return cur_value * i[1]
                else:
                    return i[1]
            else:
                available_exchanges.append(i[0])

        # print(available_exchanges)

        # iterate over currency and check for each available_exchanges
        return main(available_exchanges[0], to_currency, i[1])
        # return "Currency conversion not supported"
    else:
        print("Invalid input")


if __name__ == '__main__':
    print(main("AUD", "CAD", None))
    print(main("AUD", "JPY", None))
    # print(main("INR", "USD"))
    # print(main("GBP", "AUD"))
    # print(main("AUD", "USD"))
    # print(main("USD", "AUD"))
