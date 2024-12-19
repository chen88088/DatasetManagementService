import axios from "axios";

const API_BASE_URL = "http://192.168.158.43:8082/datasets";

// 分類相關 API
export const fetchCategories = () => axios.get(`${API_BASE_URL}/categories`);
export const fetchCategory = (categoryId) => axios.get(`${API_BASE_URL}/categories/${categoryId}`);
export const createCategory = (data) => axios.post(`${API_BASE_URL}/categories`, data, { headers: { "Cache-Control": "no-cache" }});
export const deleteCategory = (categoryId) => axios.delete(`${API_BASE_URL}/categories/${categoryId}`);

// 版本相關 API
export const fetchVersions = (categoryName) => axios.get(`${API_BASE_URL}/${categoryName}/versions`);
export const fetchVersion = (categoryName, version) => axios.get(`${API_BASE_URL}/${categoryName}/versions/${version}`);
export const createVersion = (categoryName, data) => axios.post(`${API_BASE_URL}/${categoryName}/versions`, data);
export const deleteVersion = (categoryName, version) => axios.delete(`${API_BASE_URL}/${categoryName}/versions/${version}`);
