//step2 กำหนด tpye ให้ตรง
import { form1 } from "./interface/form.interface";
import { create } from "zustand";

export const FormStore = create<form1>((...args) => {
  const [set, get] = args;
  return {
    data: {
      input1: '',
      input2: '',
    },
    setdata(data) {
      set({ data });
    },
  };
});
