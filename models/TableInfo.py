

class TableInfo:
    def __init__(self, name, object_id, principal_id, schema_id, parent_object_id,
                 type, type_desc, create_date, modify_date, is_ms_shipped, is_published,
                 is_schema_published, lob_data_space_id, filestream_data_space_id,
                 max_column_id_used, lock_on_bulk_load, uses_ansi_nulls, is_replicated,
                 has_replication_filter, is_merge_published, is_sync_tran_subscribed,
                 has_unchecked_assembly_data, text_in_row_limit, large_value_types_out_of_row,
                 is_tracked_by_cdc, lock_escalation, lock_escalation_desc, is_filetable,
                 is_memory_optimized, durability, durability_desc, temporal_type,
                 temporal_type_desc, history_table_id, is_remote_data_archive_enabled,
                 is_external, history_retention_period, history_retention_period_unit,
                 history_retention_period_unit_desc, is_node, is_edge, data_retention_period,
                 data_retention_period_unit, data_retention_period_unit_desc, ledger_type,
                 ledger_type_desc, ledger_view_id, is_dropped_ledger_table):
        self.name = name
        self.object_id = object_id
        self.principal_id = principal_id
        self.schema_id = schema_id
        self.parent_object_id = parent_object_id
        self.type = type
        self.type_desc = type_desc
        self.create_date = create_date
        self.modify_date = modify_date
        self.is_ms_shipped = is_ms_shipped
        self.is_published = is_published
        self.is_schema_published = is_schema_published
        self.lob_data_space_id = lob_data_space_id
        self.filestream_data_space_id = filestream_data_space_id
        self.max_column_id_used = max_column_id_used
        self.lock_on_bulk_load = lock_on_bulk_load
        self.uses_ansi_nulls = uses_ansi_nulls
        self.is_replicated = is_replicated
        self.has_replication_filter = has_replication_filter
        self.is_merge_published = is_merge_published
        self.is_sync_tran_subscribed = is_sync_tran_subscribed
        self.has_unchecked_assembly_data = has_unchecked_assembly_data
        self.text_in_row_limit = text_in_row_limit
        self.large_value_types_out_of_row = large_value_types_out_of_row
        self.is_tracked_by_cdc = is_tracked_by_cdc
        self.lock_escalation = lock_escalation
        self.lock_escalation_desc = lock_escalation_desc
        self.is_filetable = is_filetable
        self.is_memory_optimized = is_memory_optimized
        self.durability = durability
        self.durability_desc = durability_desc
        self.temporal_type = temporal_type
        self.temporal_type_desc = temporal_type_desc
        self.history_table_id = history_table_id
        self.is_remote_data_archive_enabled = is_remote_data_archive_enabled
        self.is_external = is_external
        self.history_retention_period = history_retention_period
        self.history_retention_period_unit = history_retention_period_unit
        self.history_retention_period_unit_desc = history_retention_period_unit_desc
        self.is_node = is_node
        self.is_edge = is_edge
        self.data_retention_period = data_retention_period
        self.data_retention_period_unit = data_retention_period_unit
        self.data_retention_period_unit_desc = data_retention_period_unit_desc
        self.ledger_type = ledger_type
        self.ledger_type_desc = ledger_type_desc
        self.ledger_view_id = ledger_view_id
        self.is_dropped_ledger_table = is_dropped_ledger_table

    def __repr__(self):
        return f"TableName: {self.name}"