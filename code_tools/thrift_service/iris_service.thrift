include "base.thrift"
namespace java stat.iris_service

enum SortingOrderType {
    ASC = 0,
    DESC = 1,
}

enum SortingFieldType {
    METRICS = 1,
    DIMENSION = 2,
}

struct Sorting {
    1: optional string field,
    2: optional SortingOrderType orderType,
    3: optional SortingFieldType fieldType,
}

enum FilterRelationShip {
    AND = 1,
    OR = 2,
}

enum ConditionOperator {
    EQ = 1,
    LT = 2,
    LE = 3,
    GT = 4,
    GE = 5,
    NE = 6,
    IN = 7,
    NOT_IN = 8,
    BETWEEN = 9,
    MATCH_IN = 10,
    MATCH_PHRASE = 11,
}

struct FilterGroup {
    1: optional string field,
    2: optional ConditionOperator conditionOperator,
    3: optional set<string> values,
    4: optional FilterRelationShip filterRelationShip,
    5: optional FilterGroup conditions,
}

struct MetricsDataRequest {
    1: required i64 flightId,
    2: required i64 groupId,
    3: optional i32 limit,
    4: optional bool versionsMerge,
    5: optional list<string> metricsList,
    6: optional list<Sorting> orderBy,
    7: optional list<string> groupByDims,
    8: optional FilterGroup filterGroup,
    9: optional bool withDefaultFilter,
    10: optional string startDate,
    11: optional string endDate,
    255: required base.Base Base,
}

struct MetricsData{
    1: optional string metricName,
    2: optional double metricValue,
}

struct Dimension{
    1: required string dimensionName,
    2: required string dimensionValue,
}

struct MetricsDataInVidAndDim {
    1: required string vid,
    2: optional list<Dimension> dimensions,
    3: optional list<MetricsData> metricsDataList,
}

struct MetricsDataResponse {
    1: optional list<MetricsDataInVidAndDim> metricsDataInVidAndDimList,
    255: required base.BaseResp BaseResp,
}

service IrisService {
    MetricsDataResponse queryMetricsData(1: MetricsDataRequest req)
}
