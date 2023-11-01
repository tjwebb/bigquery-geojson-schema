import json


def get_schema(filename):
    schema = []
    keys = ['geom']

    with open(filename) as file:
        # TODO add check for FeatureCollection
        # if file.length = 1 etc

        for line in file:
            line_json = json.loads(line)
            props = line_json['properties']

            for key, value in props.items():
                if key in keys:
                    continue

                keys.append(key)

                if isinstance(value, str):
                    schema.append({ 'name': key, 'type': 'STRING' })
                elif isinstance(value, int):
                    schema.append({ 'name': key, 'type': 'INT64' })
                elif isinstance(value, float):
                    schema.append({ 'name': key, 'type': 'FLOAT64' })

        schema.append({
            'name': 'geom',
            'type': 'GEOGRAPHY'
        })

        return schema


if __name__ == '__main__':
    import logging
    import argparse

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    print(json.dumps(get_schema(args.filename), indent=4))
