  async def prepare_csv_file(
    self, key: str | None, start_at: datetime | None, end_at: datetime | None, pagination_params: PaginationParams
  ):
    pagination = await self.list_and_search_users(key, start_at, end_at, pagination_params)

    columns = ['ID', 'Tên', 'Email', 'Số điện thoại', 'Khóa học']
    data = self.prepare_data(pagination.items)

    return pd.DataFrame(data, columns=columns)

  @get('export')
  async def export_users(
    self,
    key: str | None = None,
    start_at: datetime | None = None,
    end_at: datetime | None = None,
    pagination_params: PaginationParams = Depends(),
  ):
    data_frame = await self.prepare_csv_file(key, start_at, end_at, pagination_params)
    file_location = None

    try:
      with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        data_frame.to_csv(temp_file, index=False)
        temp_file.flush()
        file_location = temp_file.name
        return FileResponse(file_location, media_type='application/octet-stream', filename='Danh_Sach_Hoc_Vien.csv')
    finally:
      if file_location and os.path.exists(file_location):
        os.remove(file_location) ## Error delete temp file
