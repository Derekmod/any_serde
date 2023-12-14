export type float = number;
export type float__DATA = number;

export function float__to_data(value: number): number {
  return value;
}

export function float__from_data(data: any): number {
  if (typeof data !== "number") {
      const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function bool__to_data(value: boolean): boolean {
  return value;
}

export function bool__from_data(data: any): boolean {
  if (typeof data !== "boolean") {
      const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function string__to_data(value: string): string {
  return value;
}

export function string__from_data(data: any): string {
  if (typeof data !== "string") {
      const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export type SampleDataclass__y_vec = float[];

export type SampleDataclass__y_vec__DATA = float__DATA[];

export function SampleDataclass__y_vec__to_data(value: SampleDataclass__y_vec): SampleDataclass__y_vec__DATA {
    return value.map(float__to_data);
}

export function SampleDataclass__y_vec__from_data(data: any): SampleDataclass__y_vec {
    if (!Array.isArray(data)) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    return data.map(float__from_data);
}

export type SampleDataclass__pathlike__1 = string[];

export type SampleDataclass__pathlike__1__DATA = string[];

export function SampleDataclass__pathlike__1__to_data(value: SampleDataclass__pathlike__1): SampleDataclass__pathlike__1__DATA {
    return value.map(string__to_data);
}

export function SampleDataclass__pathlike__1__from_data(data: any): SampleDataclass__pathlike__1 {
    if (!Array.isArray(data)) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    return data.map(string__from_data);
}

export type SampleDataclass__pathlike = (
    | {
        type: 0;
        value: string;
    }
    | {
        type: 1;
        value: SampleDataclass__pathlike__1;
    }
);

export type SampleDataclass__pathlike__DATA = (
    | string
    | SampleDataclass__pathlike__1__DATA
);

export function SampleDataclass__pathlike__to_data(value: SampleDataclass__pathlike): SampleDataclass__pathlike__DATA {
    switch (value.type) {
        case 0:
            return string__to_data(value.value);
        case 1:
            return SampleDataclass__pathlike__1__to_data(value.value);
        default:
            const _: never = value;
            throw Error();
    }
}

export function SampleDataclass__pathlike__from_data(data: any): SampleDataclass__pathlike {
    const results: SampleDataclass__pathlike[] = [];
    try {
        results.push({
            type: 0,
            value: string__from_data(data),
        });
    } catch (rawExc: any) {
        const exc = rawExc as unknown as Error;
        if (exc.name !== "any_serde.DeserializationError") {
            throw exc;
        }
    }
    try {
        results.push({
            type: 1,
            value: SampleDataclass__pathlike__1__from_data(data),
        });
    } catch (rawExc: any) {
        const exc = rawExc as unknown as Error;
        if (exc.name !== "any_serde.DeserializationError") {
            throw exc;
        }
    }

    if (results.length !== 1) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }

    return results[0];
}

export type SampleDataclass = {
    x: float;
    y_vec: SampleDataclass__y_vec;
    description: string;
    validated: boolean;
    pathlike: SampleDataclass__pathlike;
};

export type SampleDataclass__DATA = {
    x: float__DATA;
    y_vec: SampleDataclass__y_vec__DATA;
    description: string;
    validated: boolean;
    pathlike: SampleDataclass__pathlike__DATA;
};

export function SampleDataclass__to_data(value: SampleDataclass): SampleDataclass__DATA {
    return {
        x: float__to_data(value.x),
        y_vec: SampleDataclass__y_vec__to_data(value.y_vec),
        description: string__to_data(value.description),
        validated: bool__to_data(value.validated),
        pathlike: SampleDataclass__pathlike__to_data(value.pathlike),
    };
}

export function SampleDataclass__from_data(data: any): SampleDataclass {
    if (
        typeof data !== "object"
        || Array.isArray(data)
        || data === null
    ) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const dataObj: object = data;

    if (!dataObj.hasOwnProperty("x")) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const fieldValue__x = float__from_data(dataObj["x"]);

    if (!dataObj.hasOwnProperty("y_vec")) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const fieldValue__y_vec = SampleDataclass__y_vec__from_data(dataObj["y_vec"]);

    if (!dataObj.hasOwnProperty("description")) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const fieldValue__description = string__from_data(dataObj["description"]);

    if (!dataObj.hasOwnProperty("validated")) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const fieldValue__validated = bool__from_data(dataObj["validated"]);

    if (!dataObj.hasOwnProperty("pathlike")) {
        const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
    }
    const fieldValue__pathlike = SampleDataclass__pathlike__from_data(dataObj["pathlike"]);

    return {
        x: fieldValue__x,
        y_vec: fieldValue__y_vec,
        description: fieldValue__description,
        validated: fieldValue__validated,
        pathlike: fieldValue__pathlike,
    };
}
