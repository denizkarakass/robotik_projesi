import mongoose from "mongoose";

const IKASchema = new mongoose.Schema(
  {
    name: {
      type: String
    },
    status: {
      type: String
    },
    x: {
      type: Int32Array
    },
    y: {
      type: Int32Array
    },
    z: {
      type: Int32Array
    },
    e_x: {
      type: Int32Array
    },
    e_nx: {
      type: Int32Array
    },
    e_y: {
      type: Int32Array
    },
    e_ny: {
      type: Int32Array
    },
    e_z: {
      type: Int32Array
    },
    e_nz: {
      type: Int32Array
    },
    a_x: {
      type: Int32Array
    },
    a_nx: {
      type: Int32Array
    },
    a_y: {
      type: Int32Array
    },
    a_ny: {
      type: Int32Array
    },
    a_z: {
      type: Int32Array
    },
    a_nz: {
      type: Int32Array
    },
    l_x: {
      type: Int32Array
    },
    l_y: {
      type: Int32Array
    },
    l_z: {
      type: Int32Array
    },
    s_x: {
      type: Int32Array
    },
    s_y: {
      type: Int32Array
    },
    s_z: {
      type: Int32Array
    },
  },
);

const IKA = mongoose.model("IKA", IKASchema);
export default IKA;