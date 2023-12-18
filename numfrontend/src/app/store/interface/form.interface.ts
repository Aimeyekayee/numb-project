//step1 กำหนด type ให้เรียบร้อย
interface fromdata {
  input1: string;
  input2: string;
}

export interface form1 {
  data: fromdata; //หยิบฟังชัน มาเก็บไว้ใน data
  setdata: (data:fromdata) => void; //setdata เอาค่าจากdata(บรรทัดบนมาเก็บ)
}
