"use client";
import React, { useState,useEffect } from "react";
import { Input, Form, Button } from "antd";
import axios from "axios";
import {FormStore} from "@/app/store/formm.store"

const App1 = () => {
  const [form] = Form.useForm();
  const [myInput, setMyInput] = useState<FormData>();
  const [state, setState] = useState<FormData>();
  
  const setdata =FormStore((state1)=> state1.setdata); //setdata set เข้าstore
  const data =FormStore((state2)=> state2.data); //ควรตั้งชื่อให้ตรงกันในส่วนของฟังก์ชันและ ค่าที่รับมาจาก store
  
  const onClick =()=>{
    const input = {
      input1: form.getFieldValue("input1"), //รับค่าจาก input ที่เราทำการกรอก
      input2: form.getFieldValue("input2"),
    };
    setdata(input); //setdata set  ค่าของinput 
  }

  useEffect(() => {
    console.log("use Effect", data);
  }, [data]);
  
  const onFinish = async () => {
    const input56 = {
      input1: form.getFieldValue("input1"),
      input2: form.getFieldValue("input2"),
    };
    const response = await axios.post("http://localhost:8000/input789", input56);
    setState(response.data);
    console.log(response.data);
    
    // console.log(input);
  };

  return (
    <div>
      <Form form={form} onFinish={onFinish}>
        <Form.Item name="input1" label="Input">
          <Input></Input>
        </Form.Item>
        <Form.Item name="input2" label="Input">
          <Input></Input>
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            send{" "}
          </Button>
        </Form.Item>
        <Button
          onClick={onClick}
        //onClick={console.log(myInput)}
        >
          Show Input
        </Button>
      </Form>
    </div>
  );
};
export default App1;