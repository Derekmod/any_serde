export function string__to_data(value: string): string {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function string__from_data(data: any): string {
  if (typeof data !== "string") {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export type int = number;
export type int__DATA = number;

export function int__to_data(value: number): number {
  if (!Number.isInteger(value)) {
    const e = Error(); e.name = "any_serde.SerializationError"; throw e;
  }
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function int__from_data(data: any): number {
  if (typeof data !== "number") {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  if (!Number.isInteger(data)) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function float__to_data(value: number): number {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function float__from_data(data: any): number {
  if (typeof data !== "number") {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function bool__to_data(value: boolean): boolean {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function bool__from_data(data: any): boolean {
  if (typeof data !== "boolean") {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function none__to_data(value: null): null {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function none__from_data(data: any): null {
  if (data !== null) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export function nonetype__to_data(value: null): null {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function nonetype__from_data(data: any): null {
  if (data !== null) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  return data;
}

export type SampleDataclass__y_vec = number[];

export type SampleDataclass__y_vec__DATA = number[];

export function SampleDataclass__y_vec__to_data(value: SampleDataclass__y_vec): SampleDataclass__y_vec__DATA {
  return value.map(float__to_data);
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
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

// eslint-disable-next-line @typescript-eslint/no-explicit-any
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
    default: {
      const _: never = value;
      throw Error();
    }
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__pathlike__from_data(data: any): SampleDataclass__pathlike {
  const results: SampleDataclass__pathlike[] = [];
  try {
    results.push({
      type: 0,
      value: string__from_data(data),
    });
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
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
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
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

export type SampleDataclass__opt = (
  | {
    type: 0;
    value: int;
  }
  | {
    type: 1;
    value: null;
  }
);

export type SampleDataclass__opt__DATA = (
  | int__DATA
  | null
);

export function SampleDataclass__opt__to_data(value: SampleDataclass__opt): SampleDataclass__opt__DATA {
  switch (value.type) {
    case 0:
      return int__to_data(value.value);
    case 1:
      return nonetype__to_data(value.value);
    default: {
      const _: never = value;
      throw Error();
    }
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__opt__from_data(data: any): SampleDataclass__opt {
  const results: SampleDataclass__opt[] = [];
  try {
    results.push({
      type: 0,
      value: int__from_data(data),
    });
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  } catch (rawExc: any) {
    const exc = rawExc as unknown as Error;
    if (exc.name !== "any_serde.DeserializationError") {
      throw exc;
    }
  }
  try {
    results.push({
      type: 1,
      value: nonetype__from_data(data),
    });
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
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

export type SampleDataclass__enum_value =
  | "SampleEnum.FIRST"
  | "SampleEnum.SECOND";

export type SampleDataclass__enum_value__DATA = SampleDataclass__enum_value;

export function SampleDataclass__enum_value__to_data(value: SampleDataclass__enum_value): SampleDataclass__enum_value__DATA {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__enum_value__from_data(data: any): SampleDataclass__enum_value {
  if (data === "SampleEnum.FIRST") {
    return data;
  }
  if (data === "SampleEnum.SECOND") {
    return data;
  }
  const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
}

export type SampleDataclass__multi_literal =
  | null
  | 1
  | false
  | "sample value"
  | "SampleEnum.FIRST";

export type SampleDataclass__multi_literal__DATA = SampleDataclass__multi_literal;

export function SampleDataclass__multi_literal__to_data(value: SampleDataclass__multi_literal): SampleDataclass__multi_literal__DATA {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__multi_literal__from_data(data: any): SampleDataclass__multi_literal {
  if (data === null) {
    return data;
  }
  if (data === 1) {
    return data;
  }
  if (data === false) {
    return data;
  }
  if (data === "sample value") {
    return data;
  }
  if (data === "SampleEnum.FIRST") {
    return data;
  }
  const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
}

export type SampleDataclass__enum_by_value =
  | 1
  | 10;

export type SampleDataclass__enum_by_value__DATA = SampleDataclass__enum_by_value;

export function SampleDataclass__enum_by_value__to_data(value: SampleDataclass__enum_by_value): SampleDataclass__enum_by_value__DATA {
  return value;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__enum_by_value__from_data(data: any): SampleDataclass__enum_by_value {
  if (data === 1) {
    return data;
  }
  if (data === 10) {
    return data;
  }
  const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
}

export type SampleDataclass = {
  x: number;
  y_vec: SampleDataclass__y_vec;
  description: string;
  validated: boolean;
  pathlike: SampleDataclass__pathlike;
  idx: int;
  opt: SampleDataclass__opt;
  enum_value: SampleDataclass__enum_value;
  multi_literal: SampleDataclass__multi_literal;
  enum_by_value: SampleDataclass__enum_by_value;
};

export type SampleDataclass__DATA = {
  x: number;
  y_vec: SampleDataclass__y_vec__DATA;
  description: string;
  validated: boolean;
  pathlike: SampleDataclass__pathlike__DATA;
  idx: int__DATA;
  opt: SampleDataclass__opt__DATA;
  enum_value: SampleDataclass__enum_value__DATA;
  multi_literal: SampleDataclass__multi_literal__DATA;
  enum_by_value: SampleDataclass__enum_by_value__DATA;
};

export function SampleDataclass__to_data(value: SampleDataclass): SampleDataclass__DATA {
  return {
    x: float__to_data(value.x),
    y_vec: SampleDataclass__y_vec__to_data(value.y_vec),
    description: string__to_data(value.description),
    validated: bool__to_data(value.validated),
    pathlike: SampleDataclass__pathlike__to_data(value.pathlike),
    idx: int__to_data(value.idx),
    opt: SampleDataclass__opt__to_data(value.opt),
    enum_value: SampleDataclass__enum_value__to_data(value.enum_value),
    multi_literal: SampleDataclass__multi_literal__to_data(value.multi_literal),
    enum_by_value: SampleDataclass__enum_by_value__to_data(value.enum_by_value),
  };
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function SampleDataclass__from_data(data: any): SampleDataclass {
  if (
    typeof data !== "object"
    || Array.isArray(data)
    || data === null
  ) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  const dataObj: object = data;

  if (!Object.hasOwn(dataObj, "x")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__x = (dataObj as {x: any})["x"];
  const fieldValue__x = float__from_data(fieldData__x);

  if (!Object.hasOwn(dataObj, "y_vec")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__y_vec = (dataObj as {y_vec: any})["y_vec"];
  const fieldValue__y_vec = SampleDataclass__y_vec__from_data(fieldData__y_vec);

  if (!Object.hasOwn(dataObj, "description")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__description = (dataObj as {description: any})["description"];
  const fieldValue__description = string__from_data(fieldData__description);

  if (!Object.hasOwn(dataObj, "validated")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__validated = (dataObj as {validated: any})["validated"];
  const fieldValue__validated = bool__from_data(fieldData__validated);

  if (!Object.hasOwn(dataObj, "pathlike")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__pathlike = (dataObj as {pathlike: any})["pathlike"];
  const fieldValue__pathlike = SampleDataclass__pathlike__from_data(fieldData__pathlike);

  if (!Object.hasOwn(dataObj, "idx")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__idx = (dataObj as {idx: any})["idx"];
  const fieldValue__idx = int__from_data(fieldData__idx);

  if (!Object.hasOwn(dataObj, "opt")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__opt = (dataObj as {opt: any})["opt"];
  const fieldValue__opt = SampleDataclass__opt__from_data(fieldData__opt);

  if (!Object.hasOwn(dataObj, "enum_value")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__enum_value = (dataObj as {enum_value: any})["enum_value"];
  const fieldValue__enum_value = SampleDataclass__enum_value__from_data(fieldData__enum_value);

  if (!Object.hasOwn(dataObj, "multi_literal")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__multi_literal = (dataObj as {multi_literal: any})["multi_literal"];
  const fieldValue__multi_literal = SampleDataclass__multi_literal__from_data(fieldData__multi_literal);

  if (!Object.hasOwn(dataObj, "enum_by_value")) {
    const e = Error(); e.name = "any_serde.DeserializationError"; throw e;
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fieldData__enum_by_value = (dataObj as {enum_by_value: any})["enum_by_value"];
  const fieldValue__enum_by_value = SampleDataclass__enum_by_value__from_data(fieldData__enum_by_value);

  return {
    x: fieldValue__x,
    y_vec: fieldValue__y_vec,
    description: fieldValue__description,
    validated: fieldValue__validated,
    pathlike: fieldValue__pathlike,
    idx: fieldValue__idx,
    opt: fieldValue__opt,
    enum_value: fieldValue__enum_value,
    multi_literal: fieldValue__multi_literal,
    enum_by_value: fieldValue__enum_by_value,
  };
}
