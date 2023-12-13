export type float = number;
export type float__DATA = number;

export function float__to_data(value: number): number {
  return value;
}

export function float__from_data(data: any): number {
  if (typeof data !== "number") {
      throw Error("any_serde.DeserializationError");
  }
  return data;
}

export function string__to_data(value: string): string {
  return value;
}

export function string__from_data(data: any): string {
  if (typeof data !== "string") {
      throw Error("any_serde.DeserializationError");
  }
  return data;
}

export type TestDataclass__y_vec = float[];

export type TestDataclass__y_vec__DATA = float__DATA[];

export function TestDataclass__y_vec__to_data(value: TestDataclass__y_vec): TestDataclass__y_vec__DATA {
    return value.map(float__to_data);
}

export function TestDataclass__y_vec__from_data(data: any): TestDataclass__y_vec {
    if (!Array.isArray(data)) {
        throw Error("any_serde.DeserializationError");
    }
    return data.map(float__from_data);
}

export type TestDataclass = {
    x: float;
    y_vec: TestDataclass__y_vec;
    description: string;
};

export type TestDataclass__DATA = {
    x: float__DATA;
    y_vec: TestDataclass__y_vec__DATA;
    description: string;
};

export function TestDataclass__to_data(value: TestDataclass): TestDataclass__DATA {
    return {
        x: float__to_data(value.x),
        y_vec: TestDataclass__y_vec__to_data(value.y_vec),
        description: string__to_data(value.description),
    };
}

export function TestDataclass__from_data(data: any): TestDataclass {
    if (
        typeof data !== "object"
        || Array.isArray(data)
        || data === null
    ) {
        throw Error("any_serde.DeserializationError");
    }
    const dataObj: object = data;
    if (!dataObj.hasOwnProperty("x")) {
        throw Error("any_serde.DeserializationError");
    }
    const fieldValue__x = float__from_data(dataObj["x"]);
    if (!dataObj.hasOwnProperty("y_vec")) {
        throw Error("any_serde.DeserializationError");
    }
    const fieldValue__y_vec = TestDataclass__y_vec__from_data(dataObj["y_vec"]);
    if (!dataObj.hasOwnProperty("description")) {
        throw Error("any_serde.DeserializationError");
    }
    const fieldValue__description = string__from_data(dataObj["description"]);

    return {
        x: fieldValue__x,
        y_vec: fieldValue__y_vec,
        description: fieldValue__description,
    };
}
