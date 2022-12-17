import mongoose from "mongoose";

const IHASchema = new mongoose.Schema(
  {
    name: {
      type: String
    },
    status: {
      type: String
    },
    x: {
      type: String
    },
    y: {
      type: String
    },
    z: {
      type: String
    },
    e_x: {
      type: String
    },
    e_nx: {
      type: String
    },
    e_y: {
      type: String
    },
    e_ny: {
      type: String
    },
    e_z: {
      type: String
    },
    e_nz: {
      type: String
    },
    a_x: {
      type: String
    },
    a_nx: {
      type: String
    },
    a_y: {
      type: String
    },
    a_ny: {
      type: String
    },
    a_z: {
      type: String
    },
    a_nz: {
      type: String
    },
    l_x: {
      type: String
    },
    l_y: {
      type: String
    },
    l_z: {
      type: String
    },
    s_x: {
      type: String
    },
    s_y: {
      type: String
    },
    s_z: {
      type: String
    },
  },
);

const IHA = mongoose.model("IHA", IHASchema);
export default IHA;